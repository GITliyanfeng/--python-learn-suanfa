# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 21:12
# @Author  : __Yanfeng
# @Site    : 
# @File    : btsearchTree.py
# @Software: PyCharm
class DictBinTree(object):
    """二叉排序树"""

    def __init__(self):
        self._root = None

    def is_empty(self):
        return not self._root

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.left
            else:
                return entry.val
        return

