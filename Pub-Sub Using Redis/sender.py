import redis

def send_message(msg):
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
   
    r.publish('news_channel', msg)
    print(f"Published: {msg}")

if __name__ == '__main__':
    send_message("Breaking News: Redis Pub/Sub is super easy!")
