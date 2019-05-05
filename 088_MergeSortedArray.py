# -*-coding:utf-8 -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        elif n == 0:
            pass
        else:
            nums1_index = nums2_index = 0
            while nums1_index < m + n:
                if nums1[nums1_index] < nums2[nums2_index]:
                    nums1_index = nums1_index + 1
                else:
                    nums1.insert(nums1_index, nums2[nums2_index])
                    nums1_index = nums1_index + 1
                    nums2_index = nums2_index + 1

                if nums1_index == m + nums2_index:
                    nums1[nums1_index:] = nums2[nums2_index:]
                    break
                elif nums2_index > n - 1:
                    nums1[:] = nums1[0:m + n]
                    break


if __name__ == '__main__':
    solution = Solution()

    nums1_1 = [1, 2, 3]
    m_1 = 3
    nums2_1 = []
    n_1 = 0
    solution.merge(nums1_1, m_1, nums2_1, n_1)
    print(nums1_1)

    nums1_2 = [1, 2, 3, 0, 0, 0]
    m_2 = 3
    nums2_2 = [2, 5, 6]
    n_2 = 3
    solution.merge(nums1_2, m_2, nums2_2, n_2)
    print(nums1_2)

    nums1_3 = [0]
    m_3 = 0
    nums2_3 = [1]
    n_3 = 1
    solution.merge(nums1_3, m_3, nums2_3, n_3)
    print(nums1_3)

    nums1_4 = [1, 0]
    m_4 = 1
    nums2_4 = [2]
    n_4 = 1
    solution.merge(nums1_4, m_4, nums2_4, n_4)
    print(nums1_4)

    nums1_5 = [2, 0]
    m_5 = 1
    nums2_5 = [1]
    n_5 = 1
    solution.merge(nums1_5, m_5, nums2_5, n_5)
    print(nums1_5)

    nums1_6 = [4,5,6,0,0,0]
    m_6 = 3
    nums2_6 = [1,2,3]
    n_6 = 3
    solution.merge(nums1_6, m_6, nums2_6, n_6)
    print(nums1_6)

