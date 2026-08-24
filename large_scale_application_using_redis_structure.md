## **Redis Based Application Structure for large scale application**
![large-scale-structure](advanced-structure.png)
```md
Let's understand this structure in detail.

So there will be so many user lets say 1000000 user.

Now the server is taking so many requests. Which will lead to high latency.

Now for this we can use Redis.

Redis is a distributed cache, which can store so many data in so many servers.

Redis will try to solve this latency issue by focusing on the cache.

But one thing will be issue which can cause latency issue, is that information may be not available in the cache.

So, when user send a request, it will be fetched from the database and cached in the cache.
But this will take time.

So first redis will try to fetch from truth source or database, now database wont be hit and also it wont share direct to user, it will share via passing towards redis then to user.

So in this way we understand how redis works with so many requests
```