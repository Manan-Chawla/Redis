import redis

def main():

    # connecting redis server
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    print(f"Working with Lists or task queue")

    r.delete('email_queue')


    r.lpush('email_queue','user1@gmail.com')
    r.lpush('email_queue','user2@gmail.com')
    r.lpush('email_queue','user3@gmail.com')

    # fetch items
    allemail=r.lrange('email_queue',0,-1)
    print(f"Current queue : {allemail}")


    # Performing POP operation (from right or back) like FIFO
    processed_email=r.rpop('email_queue')
    print(f"Processed email : {processed_email}")
    print(f"Remaining in Queue: {r.lrange('email_queue', 0, -1)}")



    print("Working with Sets")

    r.delete('post:101:tags')

    # add item in set
    r.sadd('post:101:tags','tech','laptop','python')


    # fetch items
    tags=r.smembers('post:101:tags')
    print(f"Current tags : {tags}")
    
    
    # check if item exists or not)
    is_tagtech=r.sismember('post:101:tags','tech')
    print(f"Is tech tag exists in set : {is_tagtech}")


if __name__ == '__main__':
    main()