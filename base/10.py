# 匿名函数
from functools import reduce

square = lambda x: x ** 2
print(square(3))


x = [(lambda x: x*x)(x) for x in range(10)]
print(x)


l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1], reverse=True)  # 按列表中元祖的第二个元素排序
print(l)


squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(squared))

l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l)  # [2, 4]
print(list(new_list))

l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x + y, l) # 1*2*3*4*5 = 120
print(product)
