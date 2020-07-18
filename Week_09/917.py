

# 917 仅仅反转字母

"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        index_dict = {}
        list1 = []
        for index, value in enumerate(S):
            if not value.isalpha():
                index_dict[index] = value
            else:
                list1.append(value)
        list1.reverse()
        for key, value in index_dict.items():
            list1.insert(int(key), value)
        return ''.join(list1)