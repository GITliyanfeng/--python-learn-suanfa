# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 0:02
# @Author  : __Yanfeng
# @Site    : 
# @File    : str_math.py
# @Software: PyCharm
'''
串匹配算法
    -逐个匹配字串和目标串
    -问题:
        -如何选择开始比较的字符对
        -如果发现不匹配,下一步该怎么做
'''

"""
朴素法:
    -从左到右逐个匹配
    -发现不匹配的,转去考虑目标串的下一个位置
"""


def naive_matching(targets, child):
    """
    缺点,存在回溯
    targets=00000000000000000000001
    child = 000001
    这种匹配的话效率最低
    """
    m, n = len(child), len(targets)
    i, j = 0, 0
    while i < m and j < n:
        if child[i] == targets[j]:
            i, j = i + 1, j + 1  # 如果匹配到,那么两个指针都后移
        else:
            i, j = 0, j - i + 1  # 如果匹配不到,i[字串索引归零],j[目标串索引减去已经匹配到的长度+1<的下一位置>]
    if i == m:
        # i 为从能够匹配到的长度 i == m就意味着可连续匹配到的长度达到字串的长度[完成匹配]
        return j - i  # 返回匹配头的位置
    return -1  # 没匹配到


# KMP 算法匹配字符串  先分析child串,从中提取有效信息,减少再targets中匹配的次数
def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - 1
    return -1


def get_pnext(p):
    """生成针对p中各个位置i的下体检查位置表,用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def get_pnext2(p):
    """
    生成针对p中各个位置i的下一检查位置表,用于KMP算法,的优化版本
    :param p:
    :return:
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == '__main__':
    targets = 'acgccagtgccatgtcaccatgattcgg'
    child = 'ccatg'
    print(naive_matching(targets=targets, child=child))
    print(matching_KMP(targets,child,get_pnext2(child)))