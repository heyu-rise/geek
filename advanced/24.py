# 垃圾回收 https://time.geekbang.org/column/article/104265
import os
import psutil
import objgraph

# 显示当前 python 程序占用的内存大小
# def show_memory_info(hint):
#     pid = os.getpid()
#     p = psutil.Process(pid)
#
#     info = p.memory_full_info()
#     memory = info.uss / 1024. / 1024
#     print('{} memory used: {} MB'.format(hint, memory))
#
#
# def func():
#     show_memory_info('initial')
#     a = [i for i in range(10000000)]
#     show_memory_info('after a created')
#
#
# func()
# show_memory_info('finished')


import sys

a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a))


def func(a):
    # 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a))


func(a)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(a))


a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])

