学习笔记


# 1. 深度优先搜索  ， 广度优先搜索的实现和特性

##  深度优先

## 广度优先



# 贪心的实现， 特性

## 贪心算法Greedy， 求最优，最好。
* 贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望
* 导致结果是全局最好或最优的算法

* 贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。
* 动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

## 贪心： 当下做局部最优判断
## 回溯： 能够回退
## 动态规划： 最优判断 + 回退


# 二分查找的实现。

## 前提：
    1. 目标函数单调性（单调递增或单调递减）
    2. 存在上下界 bounded
    3. 能够通过索引访问   index accessible


# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
*  中间值 mid， 左值 left, 右值 right
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]
1. 左值 < 中值, 中值 < 右值 ：没有旋转，最小值在最左边，可以收缩右边界
2. 左值 > 中值, 中值 < 右值 ：有旋转，最小值在左半边，可以收缩右边界
3. 左值 < 中值, 中值 > 右值 ：有旋转，最小值在右半边，可以收缩左边界
4. 左值 > 中值, 中值 > 右值 ：单调递减，不可能出现
分析前面三种可能的情况，会发现情况1、2是一类，情况3是另一类。

如果中值 < 右值，则最小值在左半边，可以收缩右边界。
如果中值 > 右值，则最小值在右半边，可以收缩左边界。
通过比较中值与右值，可以确定最小值的位置范围，从而决定边界收缩的方向。

而情况1与情况3都是左值 < 中值，但是最小值位置范围却不同，这说明，如果只比较左值与中值，不能确定最小值的位置范围。

所以我们需要通过比较中值与右值来确定最小值的位置范围，进而确定边界收缩的方向。

接着分析解法里的一些问题：

首先是while循环里的细节问题。

这里的循环不变式是left < right, 并且要保证左闭右开区间里面始终套住最小值。

中间位置的计算：mid = left + (right - left) / 2
这里整数除法是向下取整的地板除，mid更靠近left，
再结合while循环的条件left < right，
可以知道left <= mid，mid < right，
即在while循环内，mid始终小于right。

因此在while循环内，nums[mid]要么大于要么小于nums[right]，不会等于。

这样else {right = mid;}这句判断可以改为更精确的
else if (nums[mid] < nums[right]) {right = mid;}。

再分析一下while循环退出的条件。

如果输入数组只有一个数，左右边界位置重合，left == right，不会进入while循环，直接输出。

如果输入数组多于一个数，循环到最后，会只剩两个数，nums[left] == nums[mid]，以及nums[right]，这里的位置left == mid == right - 1。

如果nums[left] == nums[mid] > nums[right]，则左边大、右边小，
需要执行left = mid + 1，使得left == right，左右边界位置重合，循环结束，nums[left]与nums[right]都保存了最小值。

如果nums[left] == nums[mid] < nums[right]，则左边小、右边大，
会执行right = mid，使得left == right，左右边界位置重合，循环结束，nums[left]、nums[mid]、nums[right]都保存了最小值。
