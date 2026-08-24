## **Why redis exists?**
Traditional database store data on hard drive, hard drive are reliable but reading from them requires physical or digital disk access which takes time.
As RAM is faster than hard drive, it is used for caching.
So, when user send a request, it will be fetched from cache and returned to user.
Redis was created to solve this speed bottleneck by keepding data directly in RAM, making data retierval faster.
