

# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)
        result = True
        if s_set == set(t):
            for i in s_set:
                result = result and (s.count(i)==t.count(i))
        else:
            result = False
        return result

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)