## **Redis is not for every problem**
1. Read pressure : When there are so many read requests, redis will face latency issue.
2. Write pressure : When there are so many write requests, redis will face latency issue.
3. Data consistency : When there are so many read and write requests, redis will face data consistency issue.
4. Background operations : Redis will face latency issue when it is performing background operations like RDB or SOF.
5. Data replication : When there are so many servers, redis will face data replication issue.