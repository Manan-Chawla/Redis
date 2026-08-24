## **Redis Key management and operation**
1. TTL : Time To Live, an expiration countdown attached to a key, once it run out, redis automatically deletes the key.
2. Eviction policy : Rules redis follow to delete older or less frequently used keys when its allocated RAM gets 100% full.
3. Atomic operations : Operation that run completely or not at all, without any interruption. Prevent two requests from interfering with each other.