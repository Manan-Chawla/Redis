import redis
import json
import time
import os

def process_task(task):
    """Simulates executing heavy background jobs."""
    task_type = task.get("type")
    payload = task.get("payload")
    
    print(f"[WORKER {os.getpid()}] Processing '{task_type}' for {payload.get('email', 'User')}...")
    
    if task_type == "EMAIL_WELCOME":
        time.sleep(2)  # Simulate sending email
        print(f"[WORKER {os.getpid()}] Welcome email sent to {payload['email']}")
        
    elif task_type == "GENERATE_REPORT":
        time.sleep(4)  # Simulate heavy PDF generation
        print(f"[WORKER {os.getpid()}] Report '{payload['report_name']}' generated.")
        
    else:
        print(f"WORKER {os.getpid()}] Unknown task type: {task_type}")

def start_worker():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    queue_name = "task_queue"
    
    print(f"[WORKER {os.getpid()}] Waiting for tasks...")
    
    while True:
        # BRPOP (Blocking Right Pop): Waits until a job arrives in the queue.
        # Timeout 0 means wait indefinitely; does not burn CPU cycles.
        result = r.brpop(queue_name, timeout=0)
        
        if result:
            _, task_json = result
            task = json.loads(task_json)
            process_task(task)

if __name__ == '__main__':
    start_worker()
