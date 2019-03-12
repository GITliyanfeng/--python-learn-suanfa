# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 15:37
# @Author  : __Yanfeng
# @Site    : 
# @File    : maketree.py
# @Software: PyCharm
''''''
"""
二叉树的性质:
+ 树高  root 到 其他所有节点的最大距离 h
+ 最大节点数 2的h次方
+ 第i层中至多有2的i次方个节点
+ 高度为h  至多有 2的h-1次方-1个节点

抽象数据类型:
ADT BinTree:
    BinTree(self,data,left,right)  构造,创建一个新的二叉树
    is_empty(self) 空检测
    num_nodes(self) 节点总数
    data(self)
    left(self)
    right(self)
    set_left(self,btree)
    set_rigth(self,btree)
    traversal(self)
    forall(self,op)
"""


class BinTNode(object):
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNode(t):
    """统计节点数"""
    if t is None:
        return 0
    else:
        return 1 + count_BinTNode(t.left) + count_BinTNode(t.right)


def sum_BtinTNode(t):
    """计算所有数据的和"""
    if t is None:
        return 0
    else:
        return t.data + sum_BtinTNode(t.left) + sum_BtinTNode(t.right)


def preoder(t, proc):
    """深度先根遍历(递归)"""
    if t is None:
        return
    proc(t.data)
    preoder(t.left)
    preoder(t.right)


def print_BinTNodes(t):
    if t is None:
        print("^", end='')
        return
    print("(" + str(t.data), end='')
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(')', end='')


from 栈和队列.makequeue import SQueue


def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None:
            continue
        qu.enqueue(n.left)
        qu.enqueue(n.right)
        proc(n.data)


"""
非递归的先根遍历要点:
+ 深度遍历
+ 遇到节点,访问节点,下一步沿着节点的left下行
+ 节点的right没有被访问,但是需要记录,入栈
+ 遇到空树时回溯,取出栈中保存的right,然后想一颗完整的二叉树一样遍历它
- 遇到空树 意味着 一颗子树遍历完成
- 如果这课子树是左子树,对应的右子树应该为栈顶元素
- 如果这棵树是右子树,说明以他为右子树的大树已经完成遍历,下一步应该处理更上层的右子树

循环控制的条件:
-假设变量t一直取值为当前遍历子树的root,栈中保存的是前面记录的没有遍历的右子树.这样,只要当前树非空(当前选择的节点树需要被遍历)或者
栈非空(还有子树没有被遍历),那么循环就应该继续

循环体:
-先处理当前节点的数据,然后沿着树的左分支下行,一路上将面遇到的右节点压入到栈(这个部分 也需要一个循环),内部循环直到遇到空树的时候回溯,
从栈中弹出一个元素(最近的右分支),进行新的不遍历
"""
from 栈和队列.makestack import SStack_from_list


def preorder_nonrec(t, proc):
    s = SStack_from_list()
    # 循环条件一  当前树非空,或者栈中还有右子树
    while t is not None or not s.is_empty():
        while t is not None:  # 内部循环,确定沿左下行[只要当前节点非空就处理当前子树树的元素]
            proc(t.data)
            s.push(t.right)  # 遇到右子树压入栈
            t = t.left  # 处理完root 处理left<一路向左>
        t = s.pop()  # 当当前节点为空[左到头了] 从栈中拿出最近的一个右节点,继续处理


# 二叉树的迭代器  {先序遍历} 1.右节点入栈, 2.输出根节点 3.切换为左节点 4.左节点完毕 5.pop右节点 6.继续遍历
def preorder_elements(t):
    s = SStack_from_list()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


# 二叉树迭代器  {中序遍历}  1.左节点入栈 2.pop左节点 3.根切换为右节点 4.继续遍历
def midporder_element(t):
    s = SStack_from_list()
    while t is not None or not s.is_empty():  # 外层循环控制遍历的继续
        while t is not None:  # 内层循环控制一路向左
            s.push(t)  # 将当前节点入栈
            t = t.left  # 访问左节点  中根 左根右,所以需要先访问左节点 所以将所有的左节点都入栈
        if not s.is_empty():  # 当左节点入栈完毕,开始从栈中将最近的左节点弹出
            a = s.pop()
            yield a.data  # 输出最近做节点的数据
            t = a.right  # 然后将根切换问右节点,继续遍历


"""
最难的后序遍历
-变量t在执行过程中要满足:
    - 栈中节点序列的左边是二叉树的已遍历的部分,右边是尚未遍历的部分
    - 如果t非空,其父节点就是栈顶节点
    - t 空时,栈顶就是应访问的节点
    
根据被访问的节点时其父节点的左子节点还是右子节点,来决定下一步应该怎么做:
    - 如果是左子节点 : 就切换到右兄弟
    - 如果是右子节点 : 处理根节点,并强制退栈
    
函数顶替的重要技术在(下行循环)-内层循环.目标是找到下一个应该被访问到的节点,循环中用到一个条件表达式,要求在有左子树时持续左下行,没有左子树的
时候向右切换.该循环的结束说明栈顶点没有左右子树,应该被访问.如果外层循环的一次迭代不进入内层循环,说明栈顶点的左右子树都已经便利完毕,应该访问
栈顶点.

要点:
- 内层循环为了找当前子树的最左最下节点,将其入栈后种终止
- 如果被访问的节点是其父节点的左节点,那么就需要遍历它的右节点
- 如果被处理的节点是其中父节点的右节点,设置t=None退栈,迫使外层循环的下次迭代访问更上层的节点
"""


def postorder_nonrec(t, proc):
    s = SStack_from_list()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)  # 只要当前节点非空,就将当前节点压人栈
            t = t.left if t.left is not None else t.right  # 如果当前节点的左节点非空就衣裤向左,否则切换成为右节点
        t = t.pop()  # 将所有节点压入栈后,开始出栈
        proc(t.data)  # 不进入内层循环,需要访问栈顶节点
        if not s.is_empty() and s.top().left == t:
            # 栈非空,并且栈顶节点的左节点时当前节点,那么说明栈顶节点的右节点没有被遍历,需要切换为右节点
            t = s.top().right
        else:
            # 栈空了,或者没有右节点需要被遍历,那么就强制退栈
            t = None


# 生成器模式后续遍历
def posorder_elements(t):
    s = SStack_from_list()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        yield t.data
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None


class BinTree(object):
    """二叉树类"""

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild


if __name__ == '__main__':
    t = BinTNode(1, BinTNode(2, BinTNode(5), BinTNode(6)), BinTNode(3))
    # print_BinTNodes(t)
    # levelorder(t, print)
    # preorder_nonrec(t, lambda x: print(x, end=' '))
    res = preorder_elements(t)
    print(list(res))
    res = midporder_element(t)
    print(list(res))
    res = posorder_elements(t)
    print(list(res))
