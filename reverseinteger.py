# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function 
# returns 0 when the reversed integer overflows.

# Example 1:
    # Input: x = 123
    # Output: 321    

# Example 2:
    # Input: x = -123
    # Output: -321

# Example 3:
    # Input: x = 120
    # Output: 21

# Example 4:
    # Input: x = 0
    # Output: 0

# TIME: O(log_10 x), as roughly log_10 digits in x num
# SPACE: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        MAX_INT = 2 ** 31 - 1 #upper bound
        MIN_INT = -2 ** 31 #lower bound
        while (x != 0):
            pop = x % 10 if x > 0 else x % -10 #popopop, deals with python giving a mod result based on 
            x = int(x / 10) #update
            if ((rev > int(MAX_INT / 10)) or (rev == int(MAX_INT / 10) and pop > 7)): #overflows past upper bound
                return 0
            if ((rev < int(MIN_INT / 10)) or (rev == int(MIN_INT / 10) and pop < -8)): #overflows past lower bound
                return 0
            rev = rev * 10 + pop #add it to the reversed int
        return rev
        
s = Solution()
print(s.reverse(123)) # 321
print(s.reverse(0)) # 0
print(s.reverse(-321)) # -123
print(s.reverse(120)) # 21
print(s.reverse(2 ** 31 - 1)) # 0
print(s.reverse(-2 ** 31)) # 0

