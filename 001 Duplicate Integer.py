# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        uniqueList = []

        flag = False

        for i in nums:

            if (i not in uniqueList):
                uniqueList.append(i)
            else:
                flag = True
                break

        return flag