# -*-coding:utf-8 -*-
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for i in range(3, numRows + 1):
                list = [1, 1]
                for j in range(1, i - 1):
                    list.insert(j, result[i - 2][j - 1] + result[i -2][j])
                result.append(list)
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
