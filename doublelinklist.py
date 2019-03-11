# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 0:23
# @Author  : __Yanfeng
# @Site    : 
# @File    : doublelinklist.py
# @Software: PyCharm
class LNode(object):
    """链表的节点类"""

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


from Llnode import LinkListHaveRear


# 双向链表
class DLinkNode(LNode):
    def __init__(self, val, prev=None, next_=None):
        super(DLinkNode, self).__init__(val, next_)
        self.prev = prev


class DLinkList(LinkListHaveRear):
    def __init__(self):
        super(DLinkList, self).__init__()

    def prepend(self, val):
        newNode = DLinkNode(val, None, self._head)
        if self._head is None:  # 空表
            self._head = newNode
            self._rear = newNode
        else:
            # 新节点的下一个节点(旧的首节点)的prev为新节点
            newNode.next.prev = newNode
            old_rear = self._rear
            self._head = newNode
            self._rear = old_rear

    def append(self, val):
        # 尾端插入,生成一个节点,新节点的prev指向当前节点
        newNode = DLinkNode(val, self._rear, None)
        if self._head is None:  # 空表
            self._head = newNode
        else:
            # 非空表的上一个节点的next指向新节点
            newNode.prev.next = newNode
        self._rear = newNode

    def pop(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow('in pop of DLinkList')
        e = self._head.val
        # 将当前节点隔掉,设置成为下一节点
        self._head = self._head.next
        if self._rear is None:  # 如果下一节点是空,也就是只有一个元素
            # 删除掉当前节点,就意味着空表
            self._head = None
        else:
            # 当前节点被删掉,意味着删除上一个节点的next引用
            self._rear.next = None
        return e

    def pop_last(self):
        # 删除尾节点
        if self._rear is None:
            raise LinkedListUnderflow('in pop_last of DLinkList')
        e = self._rear.val
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


if __name__ == '__main__':
    mainList = DLinkList()
    mainList.prepend(1)
    mainList.prepend(2)
    mainList.prepend(3)
    mainList.append(5)
    mainList.append(6)
    mainList.append(7)
    mainList.pop_last()
    mainList.pop()
    print(mainList._rear.val)
    mainList.printall()