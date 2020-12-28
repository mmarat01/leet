class Solution:
# Determine whether an integer is a palindrome. An integer is a palindrome 
# when it reads the same backward as forward.

# Follow up: Could you solve it without converting the integer to a string?

    '''
    SOLUTION 1: REVERSE FULL INTEGER AND CHECK FOR 32-BIT INT OVERFLOW

        if x < 0:
            return False
        if x == self.reverse(x):
            return True
        return False
        
    def reverse(self, x: int) -> int:
        rev = 0
        MAX_INT = 2 ** 31 - 1
        while (x):
            pop = x % 10
            x = int(x/10)
            if rev > int(MAX_INT / 10) or (rev == int(MAX_INT / 10) and pop > 7):
                return 0
            rev = rev * 10 + pop
        return rev
    '''
    # TIME: O(log_10 x), as roughly log_10 digits in x num
    # SPACE: O(1)
    
    '''
    SOLUTION 2  : REVERSE HALF INTEGER ONLY TO AVOID OVERFLOW
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): #negatives and numbers ending in 0 that aren't 0
            return False
        revh = 0
        while x > revh: #while left hand is greater than reversed right hand
            pop = x % 10
            x = int(x / 10)
            revh = revh * 10 + pop
        return x == revh or x == int(revh / 10) #even digits case and odd digits case

s = Solution()
print(s.isPalindrome(121)) # true
print(s.isPalindrome(-121)) # false
print(s.isPalindrome(10)) # false
print(s.isPalindrome(-101)) # false
print(s.isPalindrome(22)) # true