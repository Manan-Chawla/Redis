import redis 
import time

def track_product(r,product_id):

    views=r.incr(f"Product : {product_id} : views")
    # incr function use to increment the value of the key by 1
    print(f"Product {product_id} has been viewed {views} times")


def is_user_rate_limited(r,user_id,limit=3,window_seconds=10):
    key=f"rate_limit:user:{user_id}"

    requests=r.incr(key)


    if requests == 1 :
        r.expire(key,window_seconds)

    if requests > limit:
        time_left=r.ttl(key)
        print(f"[BLOCKED] User {user_id} sent too many requests! Try again in {time_left}s.")
        return True
    
    print(f"[ALLOWED] Requests {requests}/{limit} processed successfully")

    return False


def main():
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    print("--- 1. Testing View Counter ---")
    track_product(r, "laptop_101")
    track_product(r, "laptop_101")
    track_product(r, "laptop_101")
    
    print("\n--- 2. Testing Rate Limiter (Limit: 3 requests per 10s) ---")
    user = "manan_dev"
    
    # Simulate 5 rapid requests from the same user
    for i in range(1, 6):
        print(f"Attempt {i}: ", end="")
        is_user_rate_limited(r, user_id=user, limit=3, window_seconds=10)
        time.sleep(1)

if __name__ == '__main__':
    main()

