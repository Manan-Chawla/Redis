## **Simple Basic Structure of Redis Based Application**

![basic-structure](basic-structure.png)

```md
Let's understand this structure in detail.

So first user send a request to the application or the backend application.

Now if the information or request is available in the cache, then it is returned to the user.

If not, then it is fetched from the database and cached in the cache.

In this Database is refer as Truth Source.


But keep this in mind that no matter what redis we have or what database we have, we will face latency issue.

Latency is the time it takes to get the information or request from the database.
```