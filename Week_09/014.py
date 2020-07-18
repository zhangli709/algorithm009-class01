

# 014 最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        start_flag = False
        for i in zip(*strs):
            if len(set(i)) == 1:
                start_flag = True
                res += i[0]
            else:
                break
        return res
