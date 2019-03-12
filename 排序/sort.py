# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 21:29
# @Author  : __Yanfeng
# @Site    : 
# @File    : sort.py
# @Software: PyCharm
""""""
"""
常用算法:
    - 插入排序
    - 选择排序
    - 交换排序
    - 分配排序
    - 归并排序
    - 外部排序
"""


# 定义结构
class record(object):
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum


# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)):  # 将一个列表分为两段  [0:1] 部分认为是已排序部分
        x = lst[i]  # 获取指针指定的当前元素
        j = i  # 获取指针指定的当前位置
        while j > 0 and lst[j - 1].key > x.key:  # while 循环寻找正确的插入位置
            # 如果进入当前循环就意味着,前者比当前,是乱序,需要将前者写到当前的位置
            lst[j] = lst[j - 1]
            j -= 1  # 即使写到当前位置,也不意味着满足更前者(4,5,2)=>(4,2,5) j需要往前移动一位继续判断 =>(2,4,5)
        # 跳出while循环,意味着找到正确的插入位置
        lst[j] = x  # 将上面记录的x树据,写到正确的位置


"""
选择排序:
    - 维护需要考虑的所有记录中最小的i可记录的已排序序列
    - 每次从未排序的序列中选取关键码最小的记录,放在已排序序列的最后
    - 以空序列作为已排序序列的开端,最终尚未排序的序列中所剩一个元素时,这个元素的关键码最大
"""


def select_sort(lst):
    for i in range(len(lst) - 1):
        k = i  # 拿出第一个
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:  # 和剩余的所有比较
                k = j  # 找到小的那个
                # 内层循环完成,也就找到那最小的元素了
        if i != k:  # 确定是否需要交换
            lst[i], lst[k] = lst[k], lst[i]


"""
交换排序
 - 冒泡排序
 - 
"""


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]


# 改进版本的冒泡排序
def bubble_sort_lv2(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                found = True
        if not found:
            break


# 块速度排序
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        lesslist = [i for i in lst[1:] if i <= pivot]
        bigglist = [i for i in lst[1:] if i > pivot]
        finallysort = quick_sort(lesslist) + [pivot] + quick_sort(bigglist)
        return finallysort


# 归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        num = int(len(lst) / 2)
        left = merge_sort(lst[:num])
        right = merge_sort(lst[num:])
        return merge(left, right)


def merge(left, right):
    leftindex, rightindex = 0, 0
    res = []
    # 一下操作是合并两个有序列表
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            res.append(left[leftindex])
            leftindex += 1
        else:
            res.append(right[rightindex])
            rightindex += 1
    res += left[leftindex:]
    res += right[rightindex:]
    return res


if __name__ == '__main__':
    lst = [98, 53, 2, 6, 1, 3, 5, 6, 122, 1, 5, 6, 2, 1, 6, 7, 8, 23, 2]
    # res = quick_sort(lst)
    res = merge_sort(lst)
    print(res)
