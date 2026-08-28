import streamlit as st
import redis

# 1. Connect to Redis (cached so Streamlit doesn't reconnect on every button click)
@st.cache_resource
def get_redis_client():
    return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r = get_redis_client()

st.title("Site Banner Manager")


st.header("Admin Panel")

message = st.text_input("Banner Message", "Flash Sale: 50% OFF everything!")
banner_type = st.selectbox("Banner Type", ["Sale", "Info", "Warning"])
expire_seconds = st.number_input("Expiration (seconds)", min_value=0, value=10)

col1, col2 = st.columns(2)

with col1:
    if st.button("Publish Banner"):
        # Save to Redis
        r.hset("site_banner", mapping={
            "message": message,
            "type": banner_type
        })
        
        # Set expiration if entered
        if expire_seconds > 0:
            r.expire("site_banner", expire_seconds)
            st.success(f"Banner published! Auto-removes in {expire_seconds} seconds.")
        else:
            st.success("Permanent banner published!")

with col2:
    if st.button("Delete Banner"):
        r.delete("site_banner")
        st.warning("Banner deleted from Redis!")

# ---------------------------------------------------------
# FRONTEND SECTION: View Active Banner
# ---------------------------------------------------------
st.divider()
st.header("Website View (Frontend)")

if st.button("Refresh / Load Website"):
    banner = r.hgetall("site_banner")
    
    if not banner:
        st.info("No active banner to display right now.")
    else:
        ttl = r.ttl("site_banner")
        ttl_text = f"Auto-removes in {ttl}s" if ttl > 0 else "Permanent"
        
        # Display colored banner based on type
        if banner.get("type") == "Warning":
            st.error(f"**{banner['message']}** ({ttl_text})")
        elif banner.get("type") == "Sale":
            st.success(f"**{banner['message']}** ({ttl_text})")
        else:
            st.info(f"**{banner['message']}** ({ttl_text})")