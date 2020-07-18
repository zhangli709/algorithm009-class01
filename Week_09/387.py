

# 字符串中的第一个唯一字符

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # 1. 暴力破解法
        # for index, value in enumerate(s):
        #     if s.count(value) == 1:
        #         return index
        # else:
        #     return -1

        # 2. hash法
        my_dict = {}
        for index, value in enumerate(s):
            if value in my_dict:
                my_dict[value] += 1
            else:
                my_dict[value] = 1
        for key, value in my_dict.items():
            if value == 1:
                return s.index(key)
        else:
            return -1