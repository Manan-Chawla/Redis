## **Genral system commands**
1. to check whether redis is running or not

```
PING
```

2. List all keys in current database

```
KEYS *
```

3. Check if specific key exists

```
EXISTS key_name
```

4. Delete specific key

```
DEL key_name
```

5. View key type

```
TYPE key_name
```

6. Clear all data in current database

```
FLUSHDB
```

--------------------------------------


## **String commands**
1. Set a key value pair

```
SET key_name value
```

2. Get value of specific key

```
GET key_name
```

3. Set Multiple key at once time

```
MSET key_name value key_name value
```

4. Get Multiple key at once time

```
MGET key_name key_name
```

5. Increment an integer value

```
INCR key_name
```

6. Increment by custom value

```
INCRBY key_name value
```

--------------------------------------



## **Key expiration and timers or TTL**
1. Set key expiration time

```
SETEX key_name seconds value
```

2. Add an expiration time to existing key

```
EXPIRE key_name seconds
```

3. Check remaining time for key expiration

```
TTL key_name
```

--------------------------------------



## **Hashes Commands**
1. Store fields and values in a hash
```
HSET hash_name field value
```

2. Read a single field value
```
HGET hash_name field
```

3. Read all fields and values
```
HGETALL hash_name
```

4. Delete a field
```
HDEL hash_name field
```


--------------------------------------


## **List Commands**
1. Push items to the left (head) or right(tail) of the list

```
LPUSH list_name value


RPUSH list_name value
```


2. Reterive items by index range (0 -1 fetches the entire list)

```
LRANGE list_name 0 -1
```


3. Remove and return first item from left 

```
LPOP list_name
```


4. Remove and return last item from right

```
RPOP list_name
```