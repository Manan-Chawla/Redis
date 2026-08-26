## **Code explanation of rate limiter**

1. **INCR** : Use to increment the value of the key by 1

2. **requests** = r.incr(key), this will track how many requests user (manan) made.

3. if requests == 1: r.expire(key, window_seconds): When the user sends their very first request, Redis attaches a 10-second timer to their key.

4. if requests > limit:: Once requests exceed 3 within that 10-second window, Redis blocks further actions and uses r.ttl(key) to inform the user how long they must wait.


5. Output : 

```python

--- 1. Testing View Counter ---
Product laptop_101 has been viewed 4 times
Product laptop_101 has been viewed 5 times
Product laptop_101 has been viewed 6 times

--- 2. Testing Rate Limiter (Limit: 3 requests per 10s) ---
Attempt 1: [ALLOWED] Requests 1/3 processed successfully
Attempt 2: [ALLOWED] Requests 2/3 processed successfully
Attempt 3: [ALLOWED] Requests 3/3 processed successfully
Attempt 4: [BLOCKED] User manan_dev sent too many requests! Try again in 7s.
Attempt 5: [BLOCKED] User manan_dev sent too many requests! Try again in 6s.

```
