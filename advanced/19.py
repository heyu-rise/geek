# 迭代器，生成器  https://time.geekbang.org/column/article/101521
# import os
# import psutil
#
#
# def is_iterable(param):
#     try:
#         iter(param)
#         return True
#     except TypeError:
#         return False
#
#
# params = [
#     1234,
#     '1234',
#     [1, 2, 3, 4],
#     set([1, 2, 3, 3, 4]),
#     {1: 1, 2: 2, 3: 3, 4: 4},
#     (1, 2, 3, 4)
# ]
#
# for param in params:
#     print('{} is iterable? {}'.format(param, is_iterable(param)))
#
#
# # 显示当前 python 程序占用的内存大小
# def show_memory_info(hint):
#     pid = os.getpid()
#     p = psutil.Process(pid)
#     info = p.memory_full_info()
#     memory = info.uss / 1024. / 1024
#     print('{} memory used: {} MB'.format(hint, memory))
#
#
# def test_iterator():
#     show_memory_info('initing iterator')
#     list_1 = [i for i in range(100000000)]
#     show_memory_info('after iterator initiated')
#     print(sum(list_1))
#     show_memory_info('after sum called')
#
#
# def test_generator():
#     show_memory_info('initing generator')
#     list_2 = (i for i in range(100000000))
#     show_memory_info('after generator initiated')
#     print(sum(list_2))
#     show_memory_info('after sum called')
#
#
# test_iterator()
# test_generator()

def is_subsequence1(a, b):
    b = iter(b)
    return all(i in b for i in a)


# def is_subsequence2(a, b):
#     b = iter(b)
#     print(b)
#
#     gen = (i for i in a)
#     print(gen)
#
#     for i in gen:
#         print(i)
#
#     gen = ((i in b) for i in a)
#     print(gen)
#
#     for i in gen:
#         print(i)
#
#     return all(((i in b) for i in a))


print(is_subsequence1([1, 3, 5], [1, 2, 3, 4, 5]))
print(all([False, False, False]))
# print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

