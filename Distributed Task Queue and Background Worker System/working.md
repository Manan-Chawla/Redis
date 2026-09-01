# **Distributed Task Queue and Background Worker System**
In this system, we have a distributed task queue implemented using Redis. The queue is used to store tasks that need to be processed in the background.

In real-world applications (like sending welcome emails, processing videos, or generating PDF invoices), you never want to force the web user to wait while a slow task runs. Instead, the main web server pushes tasks into a Redis-backed queue, and background workers pull and process those jobs in parallel.

--------------

## **Key Concepts Applied in This Project**
1. Queue Pattern (LPUSH + BRPOP): LPUSH adds jobs to the head of a Redis list, while workers run BRPOP to pull jobs from the tail (FIFO). BRPOP keeps the connection open efficiently without high CPU utilization while waiting for work.

2. JSON Serialization: Complex Python dictionaries are converted into standard JSON strings so any programming language can parse them out of Redis.

3. Scalability: You can open 3 or 4 separate terminal windows running python3 worker.py at the same time. Redis will automatically distribute incoming jobs evenly across all active workers.