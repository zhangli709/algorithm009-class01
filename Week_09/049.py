
# 049  字母异位词分组

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = [''.join(sorted(i)) for i in strs]
        from collections import defaultdict
        my_dict = defaultdict(list)
        for idx, val in enumerate(new_strs):
            my_dict[val].append(strs[idx])

        return list(my_dict.values())