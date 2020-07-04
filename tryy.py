from datetime import datetime
def do_while(fn):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        results = fn(*args, **kwargs)
        print('время выполнения = ', datetime.now() - start)
        return results
    return wrapper
def current_time(fn):
    def wrapper(*args, **kwargs):
        current_time = datetime.strftime(datetime.now(), '%Y, %m, %d, %H, %M, %S')
        print(current_time)
        result = fn(*args, **kwargs)
        return result
    return wrapper