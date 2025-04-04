import logging
import time



def apply_waiter(condition=lambda x: x, wait_time=5, interval=0.5):
    logging.debug(f"apply_waiter condition: {condition} method started")

    def decorator(func):
        def wrapper(*args, **kwargs):
            max_attempts = int(wait_time / interval)
            attempts = 1

            result = func(*args, **kwargs)
            while not condition(result):
                if attempts > max_attempts:
                    raise TimeoutError("The condition was not met within the allotted time.")
                time.sleep(interval)
                result = func(*args, **kwargs)
                attempts += 1
            logging.debug(f"apply_waiter condition: {condition} method finished with {attempts} attempts")
            return result

        return wrapper

    return decorator