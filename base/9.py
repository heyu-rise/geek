# 自定义函数 https://time.geekbang.org/column/article/97764
MIN_VALUE = 1
MAX_VALUE = 10


def validation_check(value):
    global MAX_VALUE
    MAX_VALUE = MAX_VALUE + 1
    if value < MIN_VALUE or value > MAX_VALUE:
        raise Exception('validation check fails')


def validation_check1():
    MIN_VALUE = -1
    print(MIN_VALUE)


validation_check1()
print(MIN_VALUE)


def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


#  闭包
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方
