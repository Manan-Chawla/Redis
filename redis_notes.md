# **REDIS**
Redis or Remote Dicitonary Server, is an ultra fast, in memory database used primarly for caching and speed up application performance.

Think of traditional Database as a huge filing cabinet, where we store all our data and when ever we need to get some data we have to go to cabinet and search for it.
Which is very time consuming and also requires a lot of disk space. 
Now, think of Redis as a sticky notes, which holds less information but reading take less than a milisecond.

**Real life example for understanding redis is the OTP for login, when we get 6 digit otp, it needs to self destruct in 5 minutes. Redis store OTP with built in timer caller as TTL and automatically deletes it after 5 minutes or when time runs out.**


**Redis store state in RAM or Tempory or Persistent Storage which make it faster than our traditional database like MYSQL etc.**

-------------------------------------------------------------------


