# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

# Internally you can think of this:

# # // nums is passed in by reference. (i.e., without making a copy)
# # int len = removeDuplicates(nums);

# # // any modification to nums in your function would be known by the caller.
# # // using the length returned by your function, it prints the first len elements.
# # for (int i = 0; i < len; i++) {
# #    print(nums[i]);
# # }



from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0 # we'll give them length i + 1 s. t. this represents the "allowed access" portion of the array: elements appear once, in a sorted fashion
        for j in range(len(nums)): # j is the ptr we move to compare against i
            if nums[i] != nums[j]:
                i += 1 # elements are different? update i, as this is allowed access
                nums[i] = nums[j] # if you have a [1, 2, 3] situation this is trivial, but this should amend any cases like [2, 2, 2, 2, 2, 2, 4] as the i will have stayed in the first 2 until finding a different element, after which we would have [2, 4, ...] -- voila!
        print(nums[:i+1])
        return i + 1
    '''
    this solution avoids the first index because the first is always unique; it's a little more intuitive but same logic
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1
        return index
    '''

s = Solution()
print(s.removeDuplicates([1, 1, 2])) # 2, [1, 2]
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0, 1, 2, 3, 4]