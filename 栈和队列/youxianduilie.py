# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 16:20
# @Author  : __Yanfeng
# @Site    : 
# @File    : youxianduilie.py
# @Software: PyCharm
class PrioQueueError(ValueError):
    pass


class PrioQeue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems.pop()


# 基于堆实现的优先队列
class PrioQueueheap(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.shiftup(e, len(self._elems) - 1)

    def shiftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.shiftdown(e, 0, len(elems))
        return e0

    def shiftdowm(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.shiftdowm(self._elems[i], i, end)


if __name__ == '__main__':
    # yxdl = PrioQeue(elist=[6, 5, 7, 9, 1, 3, 8])
    # yxdl.enqueue(100)
    # while not yxdl.is_empty():
    #     print(yxdl.dequeue())
    pass
