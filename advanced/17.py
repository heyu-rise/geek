# 装饰器
# def func(message):
#     print('Got a message: {}'.format(message))
#
#
# send_message = func
# send_message('hello world')
#
#
# def get_message(message):
#     return 'Got a message: ' + message
#
#
# def root_call(func, message):
#     print(func(message))
#
#
# root_call(get_message, 'hello world')
#
#
# def func_closure():
#     def get_message(message):
#         print('Got a message: {}'.format(message))
#
#     return get_message
#
#
# send_message = func_closure()
# send_message('hello world')


# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#
#     return wrapper
#
#
# def greet():
#     print('hello world')
#
#
# greet = my_decorator(greet)
# greet()
#
#
# def my_decorator(func):
#     def wrapper(message):
#         print('wrapper of decorator')
#         func(message)
#
#     return wrapper
#
#
# @my_decorator
# def greet(message):
#     print(message)


# greet('hello world xxx')
import functools


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print("wrapper of decorator")
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet('xxx')
help(greet)


class Count:
    def __init__(self, func):
        self.func = func
        self.num = 0

    def __call__(self, *args, **kwargs):
        self.num += 1
        print('num: {}'.format(self.num))
        return self.func(*args, **kwargs)


@Count
def example():
    print('hello world')


example()
example()

import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')
