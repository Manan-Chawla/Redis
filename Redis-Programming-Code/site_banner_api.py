# Site Banner : Those top pop up which usually showcase sale and advertisement, it can be static and dynmaic too.

import redis
import time

def set_banner(r, message, expire_seconds=None):
    """Stores the active site banner."""
    r.hset("site_banner", mapping={
        "message": message,
        "type": "sale"
    })
    
    # If a time limit is provided, auto-delete the banner after N seconds
    if expire_seconds:
        r.expire("site_banner", expire_seconds)
        print(f"[ADMIN] Banner published! Auto-removes in {expire_seconds} seconds.")
    else:
        print("[ADMIN] Permanent banner published!")

def get_banner(r):
    """Fetches and displays the active site banner."""
    banner = r.hgetall("site_banner")
    
    if not banner:
        print("[WEBSITE] No active banner found.")
    else:
        print(f"[WEBSITE] Active Banner: '{banner['message']}' ({banner['type']})")

def main():
    # 1. Connect to local Redis
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    print("--- Step 1: Set a Flash Sale Banner (5 Seconds Limit) ---")
    set_banner(r, "Flash Sale: 50% OFF everything!", expire_seconds=5)
    get_banner(r)

    print("\n--- Step 2: Waiting 6 Seconds for Banner to Expire... ---")
    time.sleep(6)

    print("\n--- Step 3: Fetch Banner After Expiration ---")
    get_banner(r)

if __name__ == '__main__':
    main()
