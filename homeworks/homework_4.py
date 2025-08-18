def check_time_before_after (function):
    def wrapper(*args, **kwargs):
        from datetime import datetime as dt
        start_time = dt.now()
        print(f'Функция была вызвана в {start_time.hour}:{start_time.minute}:{start_time.second} {start_time.day}/{start_time.month}/{start_time.year}')
        result = function(*args, **kwargs)
        end_time = dt.now()
        print(f'Функция была завершина в {end_time.hour}:{end_time.minute}:{end_time.second} {end_time.day}/{end_time.month}/{end_time.year}')
        return result
    return wrapper

from time import sleep

@check_time_before_after
def hello_world():
    print('hello world')
    sleep(3)

hello_world()