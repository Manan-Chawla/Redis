## **Redis Storage and Architecture**
1. In-memory : Storing data directly in RAM rather than on a hard drive.
2. Key Value Pair : Core format redis uses to store data.
```python
"product_id": "1234567890"
"session_id": "1234567890"
"session_name": "user_1234567890"
```
3. Presistence Mechanism : RDB or SOF that copy RAM data to harddrive so nothing lost if the server reboots.