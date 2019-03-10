# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 19:48
# @Author  : __Yanfeng
# @Site    : 
# @File    : Llnode.py
# @Software: PyCharm

class LNode(object):
    """链表的节点类"""

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def testcase_LNode():
    # 实现单链表
    rootNode = LNode(1)
    root = rootNode
    for i in range(2, 11):
        root.next = LNode(i)
        root = root.next

    root = rootNode
    while root is not None:
        print(root.val)
        root = root.next


class LinkedListUnderflow(ValueError):
    pass


class LList(object):
    def __init__(self):
        # _head对应当前节点
        self._head = None

    def is_empty(self):
        return self._head is None

    # 前端插入
    def prepend(self, val):
        # 实例化一个新的节点LNode,将新节点的next指向当前节点,将当前节点设置成为新节点
        newLNode = LNode(val, self._head)
        self._head = newLNode

    def pop(self):
        # 删除元素当前
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.val
        # 指针指向下下个
        self._head = self._head.next
        return e

    # 后端插入
    def append(self, val):
        if self._head is None:
            # 空链表生成新的节点
            self._head = LNode(val)
        p = self._head
        # 循环遍历到整个链表的末尾
        while p.next is not None:
            p = p.next
        # 在末尾节点添加一个新的节点
        p.next = LNode(val)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        # 如果当前节点的下一个节点是空,那就找到末节点
        if p.next is None:
            # 获取当前节点的值
            e = p.val
            # 将当前节点设置成空
            self._head = None
            return e
        # 循环 判断当前节点的下一下一节点是否非空
        while p.next.next is not None:
            # 如果非空的话就向下遍历
            # 如果为空,那么当前节点就是倒数第二节点,也就是删除末尾后的新末尾节点,不再遍历
            p = p.next
        # 跳出循环后,将当前节点的下一节点(末节点)的值取出
        e = p.next.val
        # 将末节点设置成空
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.val):
                return p.val
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            # 输出当前节点的值,不换行
            print(p.val, end='')
            # 如果当前节点的下一个节点非空
            if p.next is not None:
                # 输出一个逗号,不换行
                print(', ', end='')
            p = p.next
        # 循环结束输出换行
        print('')

    # 链表的遍历操作 ,proc是一个针对表内所有节点的值的操作
    # 例如 lambda x: print(f'val is {x}')
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.val)
            p = p.next

    def values(self):
        # 生成器的方式返回链表中的值
        p = self._head
        while p is not None:
            yield p.val
            p = p.next

    def find_all(self, pred):
        # 遍历筛选,返回生成器
        p = self._head
        while p is not None:
            if pred(p.val):
                print(p.val)
                yield p.val
            p = p.next


class LinkListHaveRear(LList):
    def __init__(self):
        super(LinkListHaveRear, self).__init__()
        self._rear = None

    def prepend(self, val):
        # 判断空表
        if self._head is None:
            self._head = LNode(val, self._head)
            self._rear = self._head
        else:
            self._head = LNode(val, self._head)

    def append(self, val):
        # 判断空表
        if self._head is None:
            self._head = LNode(val, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(val)
            self._rear = self._rear.next

    def pop_last(self):
        # 判断空表
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        # 判断表中只有一个元素的情况
        if p.next is None:
            e = p.val
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.val
        p.next = None
        return e


if __name__ == '__main__':
    mlist_1 = LList()
    for i in range(10):
        # 首端插入
        mlist_1.prepend(i)
    for i in range(11, 20):
        # 尾端插入
        mlist_1.append(i)
    # 打印 方法测试
    # mlist_1.pop_last()
    # mlist_1.pop()
    # r = mlist_1.find(lambda x: x == 14)
    # print(r)
    mlist_1.printall()

    # 遍历操作测试
    # mlist_1.for_each(lambda x: print(f'val is {x}'))
    # 生成器测试
    # r = mlist_1.values()
    # print(next(r))
    # print(next(r))
    # print(next(r))
    # r = [ i for i in mlist_1.values()]
    # print(r)
    # find_all 测试
    # r = mlist_1.find_all(lambda x: x % 2 == 0)
    # print(list(r))
    mlist_2 = LinkListHaveRear()
    mlist_2.prepend(100)
    for i in range(10):
        mlist_2.append(i)
    mlist_2.printall()
