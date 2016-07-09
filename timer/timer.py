import time


def make_timer():
    """Keep track of time between calls"""
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return
        result = now - last_called
        last_called = now
        return result

    return elapsed


timer_func = make_timer()
print(timer_func())
print(timer_func())
print(timer_func())
