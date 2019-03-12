# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 15:09
# @Author  : __Yanfeng
# @Site    : 
# @File    : makequeue.py
# @Software: PyCharm

class QueueUndeflow(ValueError):
    pass


class SQueue(object):
    def __init__(self, init_len=8):
        self._len = init_len
        self._elem = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        """访问头元素"""
        if self._num == 0:
            raise QueueUndeflow
        return self._elem[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUndeflow
        e = self._elem[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        # 在正确的位置加入新的元素
        self._elem[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        # 队列满了,需要扩充
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elem[(self._head + i) % old_len]
        self._elem, self._head = new_elems, 0


if __name__ == '__main__':
    myqu = SQueue()
    myqu.enqueue(1)
    myqu.enqueue(2)
    myqu.enqueue(3)
    myqu.enqueue(4)
    while not myqu.is_empty():
        print(myqu.dequeue())
