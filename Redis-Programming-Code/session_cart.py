import redis
import time


def create_user_session(r,user_id,name,email):
    session_key=f"session:{user_id}"

    # set to store data or session information
    r.hset(session_key, mapping={
        "name":name,
        "email":email,
        "status":"active"
    })

    r.expire(session_key,30)
    print(f"[SESSION CREATED] user '{name}' with session key '{session_key}' in 30 seconds")



# adding items in the cart 
def add_item_cart(r, user_id, product_id, price):
    cart_key = f"cart:{user_id}"
    r.hset(cart_key, product_id, price)

    r.expire(cart_key, 10)
    print(f"[ITEM ADDED] {product_id} x {price} to cart for user {user_id}")



# getting cart item summary
def get_cart(r,user_id):
    cart_key=f"cart:{user_id}"
    cart_items = r.hgetall(cart_key)
    
    if not cart_items:
        print(f"[CART EMPTY] Cart for user '{user_id}' has expired or is empty.")
        return None
        
    total_price = sum(float(price) for price in cart_items.values())
    ttl = r.ttl(cart_key)
    print(f"[CART SUMMARY] Items: {cart_items} | Total: ${total_price:.2f} | Auto-clears in: {ttl}s")


# main program

# connecting redis server
r=redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# setting user id
user_id=101

# creating user session
create_user_session(r,user_id,"Manan","chawlamanan26@gmail.com")

# adding item to cart
add_item_cart(r,user_id,"HP Pavillion",89000)

# getting cart item summary
get_cart(r,user_id)
