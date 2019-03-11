# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 21:30
# @Author  : __Yanfeng
# @Site    : 
# @File    : insert_sort.py
# @Software: PyCharm

def ins_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]  # 从第二个元素开始辨遍历,获取当前值          值 x
        j = i  # 获取当前位置[判断点]                         位置 j
        while j > 0 and lst[j - 1] > x:  # 循条件           列表中还有元素而且当前值<前一个值   [后面比前面小]
            lst[j] = lst[j - 1]  # 执行交换                 将大的[前面]赋值给当前[后面]
            j -= 1  # 判断点j向前移动                        上述的判断完成后,继续判断是否前面还有比x大的元素,然后再执行[向后]赋值
        lst[j] = x  # 最终循环结束,将x值放在应该它存在的位置      正确位置[前者<=x<后者]


if __name__ == '__main__':
    a = [1, 8, 3, 5, 5, 6, 3, 3, 7, 9, 0]
    ins_sort(a)
    print(a)
