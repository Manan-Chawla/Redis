import redis
import json
import time

def enqueue_task(r, task_type, payload):
    task = {
        "type": task_type,
        "payload": payload,
        "created_at": time.time()
    }
    
    r.lpush("task_queue", json.dumps(task))
    
    r.incr("metrics:tasks_created")
    print(f"📥 [PRODUCER] Queued task: {task_type}")

def main():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    print("--- Dispatching Background Jobs ---")
    
    # This task will be accepted by the worker process
    enqueue_task(r, "EMAIL_WELCOME", {"email": "manan@example.com", "name": "Manan"})
    
    # This task will be accepted by the worker process
    enqueue_task(r, "GENERATE_REPORT", {"report_name": "Q3_Financial_Summary.pdf", "user_id": 101})
    
    # This task will be accepted by the worker process
    enqueue_task(r, "EMAIL_WELCOME", {"email": "dev@example.com", "name": "Dev"})

    # This task will not be accepted by the worker process
    enqueue_task(r, "EMAIL_REOPEN", {"email": "dev@example.com", "name": "Dev"})

if __name__ == '__main__':
    main()