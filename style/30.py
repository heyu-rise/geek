# 单元测试 https://time.geekbang.org/column/article/107929
import unittest


def sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [3, 5, 2, 6, 2]
        self.assertEqual(sort(arr), [2, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()
