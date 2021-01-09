from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        doin addition
        basically
        '''
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        digits.insert(0,1)
        return digits

s = Solution()
print(s.plusOne([4,3,2,1])) # [4, 3, 2, 2]
print(s.plusOne([0])) # [1]
print(s.plusOne([3,2,0])) # [3, 2, 1]
print(s.plusOne([1,9,9])) # [2, 0, 0]
print(s.plusOne([9,9,9,9])) # [1, 0, 0, 0, 0]
