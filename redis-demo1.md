## **Breakdown of Redis Demo Program**


1. Importing redis module
   
   `import redis`


2. Define a main function, where all redis interaction take place


3. Establishing connection with redis server

   `r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)`

   here, 
   
   **host='localhost'** : specifies redis is running on your local machine

   **port=6379** : specifies redis is running on port 6379
  
   **db=0** : specifies we are using database 0
   
   **decode_responses=True** : specifies we are decoding the response from redis server as string

   **But to use this function, we have to start our redis server by using ubuntu shell, open ubuntu shell and type the following command:**

   `sudo service redis-server start`


4. Execution guard, where we are checking if the program is running from the main thread

   ```python
   if __name__ == '__main__':
        main()
   ```