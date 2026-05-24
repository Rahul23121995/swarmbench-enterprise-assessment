import threading

def run_parallel_tasks(tasks):
    for task in tasks:
        thread = threading.Thread(target=_execute_task, args=(task,))
        thread.start()

def _execute_task(task):
    result = task()
    # Broken: unprotected log writes under high concurrency
    with open('test_run.log', 'a') as f:
        f.write(f"Task result: {result}\n")
