# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 15:38
# @Author  : __Yanfeng
# @Site    : 
# @File    : testsqrt.py
# @Software: PyCharm


def get_sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2
    return y


if __name__ == '__main__':
    print(get_sqrt(2))
