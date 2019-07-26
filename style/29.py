# 上下文with语句 https://time.geekbang.org/column/article/106821
from contextlib import contextmanager


class FileManager:

    def __init__(self, name, mode):
        print('init')
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('enter')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        if self.file:
            self.file.close()


# with FileManager('d:/aaa.txt', 'w') as f:
#     print('ready')
#     f.write('hello word')


class Foo:

    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        if exc_type:
            print(f'exec_type: {exc_type}')
            print(f'exc_val: {exc_val}')
            print(f'exc_tb: {exc_tb}')
            print('exception handle')
        return True


# with Foo() as f:
#     # raise Exception('xxxx')
#     print('xxx')

@contextmanager
def file_manage(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manage('d:/aaa.txt', 'w') as h:
    h.write('hello word')
