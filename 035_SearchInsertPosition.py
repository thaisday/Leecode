# -*-coding:utf-8 -*-
from typing import List

__author__ = 'KiddoMa'
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0
        elif target is None:
            return 0
        elif target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target == nums[-1]:
            return len(nums)-1
        else:
            start_index = 0
            end_index = len(nums)
            while True:
                middle =(start_index+end_index)//2
                if target > nums[middle]:
                    start_index = middle
                elif target < nums[middle]:
                    end_index = middle
                else:
                     return middle
                if end_index - start_index == 1:
                    return start_index + 1
if __name__ == '__main__':
    solution = Solution()
    nums_1 = [1,3,5,6]
    target_1 = 5
    print(solution.searchInsert(nums_1,target_1))

    nums_2 = [1,3,5,6]
    target_2 = 2
    print(solution.searchInsert(nums_2,target_2))

    nums_3 = [1,3,5,6]
    target_3 = 7
    print(solution.searchInsert(nums_3,target_3))

    nums_4 = [1,3,5,6]
    target_4 = 0
    print(solution.searchInsert(nums_4,target_4))

    nums_5 = [1,2,4,6,7]
    target_5 = 3
    print(solution.searchInsert(nums_5, target_5))