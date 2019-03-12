# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 20:45
# @Author  : __Yanfeng
# @Site    : 
# @File    : makehuffman.py
# @Software: PyCharm
""""""
"""
哈夫曼树  带权扩充二叉树   权即当前节点的data乘以所在的层数
"""
from 二叉树.maketree import BinTNode
from 栈和队列.youxianduilie import PrioQeue


# 借助二叉扩充树
class HFFTNode(BinTNode):
    # 为哈夫曼树的节点增加一个<的计算方法
    def __lt__(self, other):
        return self.data < other.data


# 借助优先队列
class HuffmanPrioQ(PrioQeue):
    # 怎加检查队列中元素个数的方法
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):
    """定义哈夫曼树生成的方法"""
    trees = HuffmanPrioQ()  # 构造一个优先队列
    for w in weights:
        # 根据权重往优先队列中添加节点
        trees.enqueue(HFFTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HFFTNode(x, t1, t2))
    return trees.dequeue()
