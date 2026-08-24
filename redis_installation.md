## **Installation of Redis locally**

1. Open Powershell and write command : 

   `wsl --install`

2. Restart your laptop, in order to apply the changes (it is very important step)

3. Ubuntu will start installing.

4. Open Powershell as admin and write the following commands in order to allow ubuntu to run with virtual machine 
   
   `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

   
   `bcdedit /set hyperlaunchtype auto`

5. Now shutdown your laptop and wait for a min and then again turn it on.

6. Open powershell again and write command : 

   `wsl --set-default-version 1`

7. Open Ubuntu app and wait untill it install and load

8. After few minutes Ubuntu shell will open and set it up by entering details
   
   `UNIX username : manan`

   `UNIX password : manan21`

9. Now write command in ubuntu shell : 
   
   `sudo apt update && sudo apt install redis-server -y`

   `enter password you have set previously for security`

   `If above command failed then run : sudo apt install redis-server -y`

10. Now run these command : 
    
    `sudo service redis-server start` : to start server 

    `redis-cli ping` : to check if server is running, if it returns "PONG", then server is running.
   
11. After PONG, returns writer command to set redis : 
   
    `redis-cli`

    It will start localserver like this : 127.0.0.1.6379 

    `127.0.0.1:6379> SET USER "manan"`

    `127.0.0.1:6379> GET USER`
    `manan`
   
    `SETEX otp 15 "2580"`

    `TTL otp`
    `15`


12. Now to use redis in your project or application, we have to activate it using ubuntu shell by command : 
    
    `sudo service redis-server start`