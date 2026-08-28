import redis
import time

def main():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    print("--- 1. Writing Data via Python ---")
    
    # 1. Set a standard string
    r.set("app:status", "online")
    print("✓ Set 'app:status' -> 'online'")

    # 2. Add items to a set (Online Users)
    r.sadd("users:online", "manan", "alex", "sarah")
    print("✓ Added users to 'users:online' set")

    # 3. Create a hash (Product inventory)
    r.hset("inventory:laptop", mapping={
        "brand": "HP Pavillion",
        "stock": 15,
        "price": 89000
    })
    print("✓ Created hash 'inventory:laptop'")

    # 4. Set a key with a 60-second expiration timer
    r.setex("temp:token", 60, "SECRET_XYZ_123")
    print("✓ Created temporary token 'temp:token' (60s TTL)")

    print("\n[SUCCESS] Python script finished! Leave this running or close it.")
    print("Now open your Ubuntu terminal and test the commands below!\n")

if __name__ == '__main__':
    main()