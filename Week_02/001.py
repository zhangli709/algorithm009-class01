

# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(nums):
            my_dict[value] = index
        for i in range(len(nums)):
            if (target-nums[i]) in my_dict and my_dict[target-nums[i]] != i:
                return [i, my_dict[target-nums[i]]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if (target-nums[i]) in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target-nums[i])]