import redis 

def send_messages(msg):
    r=redis.Redis(host='localhost', port=6379, db=0)
    pub=r.pubsub()
    pub.publish('radio_station', msg)
    r.close()
    
if __name__ == '__main__':
    send_messages('Hello, World!')
