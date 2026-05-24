import functools

def retry_on_failure(retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:  # Fixed: catch all exceptions including AssertionError
                    attempts += 1
                    if attempts >= retries:
                        raise e
                    print(f"Test failed, retrying attempt {attempts}/{retries}...")
        return wrapper
    return decorator
