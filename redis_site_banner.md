## **Site Banner in Redis**
Site banner is a banner that is displayed on the website to notify the users about the latest updates or promotions.
In redis we can store the site banner in a hash.
The hash key will be the site banner id and the hash value will be the site banner content.
It does have TTL which is the time to live of the site banner.


---------------


## **Real World Use of Site Banner**
In the real world, we can use site banner to notify the users about the latest updates or promotions.
1. We can use site banner to notify the users about the latest products or services.
2. We can use site banner to notify the users about the latest news or events.
3. We can use site banner to notify the users about the latest security updates.
4. We can use site banner to notify the users about the latest legal updates.


---------------


## **Working of Site Banner Code with Redis and Streamlit**
1. We have to import redis and install streamlit (if not installed already).
2. We have to create a redis connection.
3. We have to create a site banner hash.
4. We have to set the site banner content.
5. We have to set the site banner TTL.
6. We have to display the site banner on the website.

---------------

## **Overall summary of workflow**
```flowchart

[ Admin Interface ] 
        │
        ▼ (hset + expire)
  [ REDIS SERVER (RAM) ] ── (Auto-deletes key after TTL seconds)
        │
        ▼ (hgetall + ttl)
[ Frontend Website View ]

```