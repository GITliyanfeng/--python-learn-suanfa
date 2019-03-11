# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 22:51
# @Author  : __Yanfeng
# @Site    : 
# @File    : josephus.py
# @Software: PyCharm

"""
约瑟夫环的问题   使用顺序表解决

n 个人坐一圈
从第k个开始报数
报到第m个数的人退出
"""


def josephus_python_list(n, k, m):
    """
    使用python的list方式解决
    不存在改变表结构
    人走了,就将数置为0[人走椅子留下]
    :param n:
    :param k:
    :param m:
    :return:
    """
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print(", ", end='')
        else:
            print('')
    return


if __name__ == '__main__':
    josephus_python_list(10, 2, 7)
