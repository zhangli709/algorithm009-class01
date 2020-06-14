


# 169 多数元素


# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. 暴力破解， 超时
        # for i in nums:
        #     if nums.count(i)*2 > len(nums):
        #         return i

        # 内置函数counter

        from collections import Counter
        my_dict = Counter(nums)
        for k,v in my_dict.items():
            if v*2 > len(nums):
                return k