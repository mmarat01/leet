from typing import List
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        traverse list starting from second element because
        first element added to sum is the first element in array
        
        we keep a moving sum ("up to this point"), defined as the maximum
        of the previous moving sum + current number OR the current number alone.
        the reason why we'd reset to the current number alone is because by 
        keeping track of the moving contiguous sum, if a new element is greater than
        the whole thing, that must be the start of the new max subarray. 
        
        with negative numbers, there could potentially be a scenario where both 
        "curr_sum + curr_num" or "curr_num" are smaller than the sum that had been
        found before.
                * say you have a current sum of "-2", and the next number is "-4"
                -2 + -4 = -6
                so -4 it is --> new current sum, and smaller than the prev
                
        that's why we want to keep track of the greatest "current sum"! if it 
        were all positives this would be trivial; you'd add them all up.
    
        '''
        if len(nums) == 1:
            return nums[0]
        
        curr_sum = max_sum = nums[0]
        '''
        cool syntax i should prob use
        
        for i in nums[1:]:
            curr_sum = max(curr_sum + i, i)
            max_sum = max(max_sum, curr_sum)
            
        '''
        for i in range(1, len(nums)): 
            if curr_sum + nums[i] < nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
                
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
        
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([0])) # 0
print(s.maxSubArray([-1])) # -1
print(s.maxSubArray([-2147483647])) # -2147483647