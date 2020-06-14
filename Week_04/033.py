
# 搜索旋转排序数组


# 1. 暴力破解
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


# 2. 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1

        if nums == []:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        if nums[l] == target:
            return l
        else:
            return -1