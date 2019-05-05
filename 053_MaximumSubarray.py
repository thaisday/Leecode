# -*-coding:utf-8 -*-
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

翻译:
给定一个整数数组,找出和最大的子数组,并返回该和的值
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            result = nums[0]
            current = 0
            for num in nums:
                current = max(current + num, num)
                result = max(result, current)
            return result


if __name__ == '__main__':
    solution = Solution()
    nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums_1))

    nums_2 = [-2, -3, -4, -5, -6, -7, -8, -9]
    print(solution.maxSubArray(nums_2))

    nums_3 = [1]
    print(solution.maxSubArray(nums_3))

    nums_4 = [1, 2]
    print(solution.maxSubArray(nums_4))
