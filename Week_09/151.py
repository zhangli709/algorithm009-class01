

# 151 反转字符串里的单词

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.strip().split()
        list1.reverse()
        return ' '.join(list1)