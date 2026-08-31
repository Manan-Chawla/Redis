import redis

def listen_messages():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    
    pubsub = r.pubsub()
    
    
    pubsub.subscribe('news_channel')
    
    print("Listening for messages on 'news_channel'...")
    
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"New Message Received: {message['data']}")

if __name__ == '__main__':
    listen_messages()
