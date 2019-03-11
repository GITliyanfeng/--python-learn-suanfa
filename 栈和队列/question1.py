# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0012 2:02
# @Author  : __Yanfeng
# @Site    : 
# @File    : 匹配括号问题.py
# @Software: PyCharm
""""""
"""
匹配括号问题  括号是否闭合
+ 顺序扫描
+ 跳过无关字符
+ 遇到左括号就push
+ 遇到右括号就pop  将pop的结果于之匹配
+ 成功继续,失败结束
"""
from 栈和队列.makestack import SStack_from_list


def check_parens(text):
    parens = "()[]{}"
    left_parens = "([{"
    paren_map = {')': '(', '}': '{', ']': '['}

    def parentheses(text):
        """
        括号生成器
        :param text:
        :return: 返回下一个括号以及位置
        """
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                # 跳过非括号元素
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack_from_list()
    m = 0
    for pr, index in parentheses(text):
        try:
            if pr in left_parens:
                st.push(pr)
            elif st.pop() != paren_map[pr]:
                print("Unmatching is found at", index, 'for', pr)
                return False
        except ValueError as f:
            print("Unmatching")
            return

    if not st.is_empty():
        print("Unmatching is found at", 0, 'for', st.pop())
        return
    print("All parentheses are correctly matched.")
    return True


if __name__ == '__main__':
    text = "[]{}[]{}{{}}{]{}{}"
    check_parens(text)
