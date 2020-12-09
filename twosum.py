# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]

# Example 3:
    # Input: nums = [3,3], target = 6
    # Output: [0,1]
 
# Constraints:
    # 2 <= nums.length <= 103
    # -109 <= nums[i] <= 109
    # -109 <= target <= 109
    # Only one valid answer exists.

# TIME: O(n)
# SPACE: O(n)

class Solution:
    def two_sum(self, nums, target):
        dict = {} #for hashing
        for i, v in enumerate(nums):
            comp = target - v #get complement of current element 
            if (comp in dict): #is the complement in the dict already (as a hashed v)
                return [dict[comp], i] #found it, return the indices in nums
            dict[v] = i #didn't find it yet, so hash the v
        return []

s = Solution()
print(s.two_sum([], 27))              # []
print(s.two_sum([5, 6], 7))           # []
print(s.two_sum([5, 6], 11))          # [0, 1]
print(s.two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(s.two_sum([2, 7, 11, 15], 27))  # []
print(s.two_sum([2, 7, 11, 15], 26))  # [2, 3]

