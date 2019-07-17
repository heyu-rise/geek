# 异常处理：如何提高程序的稳定性?

try:
    10 / 0
except Exception as error:
    print(error)
    pass


class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    # java的toString()
    def __str__(self):  # 自定义异常类型的 string 表达形式
        return "{} is invalid input".format(repr(self.value))


try:
    raise MyInputError(1)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))
finally:
    print('finally')

