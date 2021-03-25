import time

def dec1_benchmark(func):
    """
    """
    def my_func():
        t =time.time()
        func()
        print(f"Время выполнения функции: {time.time() - t}")
    return my_func


def dec2_log(func):
    def my_func():
        print("Начало выполнения функции")
        func()
        print("Функция выполнена")
    return my_func

def dec3_counter(func):
    # if hasattr(func,"counter"):
    #     func.counter = func.counter + 1
    # else:
    #     func.counter = 0

    def my_func():
        if hasattr(func,"counter"):
            func.counter = func.counter + 1
        else:
            func.counter = 1
        func()
        print(f"Функция выполнена: {func.counter} раз")
    return my_func


@dec1_benchmark
@dec2_log
@dec3_counter
def my_func1():
    time.sleep(1)
    print("Hello")


my_func1()

