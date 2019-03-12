# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 21:04
# @Author  : __Yanfeng
# @Site    : 
# @File    : makedict.py
# @Software: PyCharm

""""""
"""
字典的主要用途是查询,字典的键不可以更改(键是字典结构的关键)
"""


class Assoc(object):
    """关联对象类"""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return f'Assoc({self.key},{self.value})'


class DictFromList(object):
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems
