# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 1:45
# @Author  : __Yanfeng
# @Site    : 
# @File    : makestack.py
# @Software: PyCharm

from l链表.Llnode import LNode


class StackUnderflow(ValueError):
    pass


class SStack_from_list(object):
    def __init__(self):
        self._elems = []  # 使用list实现栈

    def is_empty(self):
        """判断栈是否为空"""
        return self._elems == []

    def top(self):
        """访问栈顶元素"""
        if not self._elems:
            raise StackUnderflow("in SStack_from_list.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        """弹出栈顶元素"""
        if not self._elems:
            raise StackUnderflow("in SStack_from_list.pop()")
        return self._elems.pop()

    def depth(self):
        return len(self._elems)


class SStack_from_Linklist(object):
    """基于链表实现栈"""

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if not self._top:
            raise StackUnderflow('in SStack_from_Linklist.top()')
        return self._top.val

    def push(self, val):
        self._top = LNode(val, self._top)

    def pop(self):
        if not self._top:
            raise StackUnderflow('in SStack_from_Linklist.pop()')
        p = self._top
        self._top = p.next
        return p.val


if __name__ == '__main__':
    st1 = SStack_from_list()
    st1.push(1)
    st1.push(2)
    st1.push(3)
    while not st1.is_empty():
        print(st1.pop())

    st2 = SStack_from_Linklist()
    st2.push(1)
    st2.push(2)
    st2.push(3)
    while not st2.is_empty():
        print(st2.pop())
