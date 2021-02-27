# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Time: O(logn) for binary search, idk about Newton's


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        square root of x is <= x
        """
        #         if x <= 1:
        #             return x

        #         # newton's method
        #         y = x//2

        #         while y*y > x: # square too high
        #             y = (y + x//y)//2 # correct

        #         return int(y)

        if x <= 1:
            return x
        low = 0
        high = x
        #  find the largest int whose
        #  square is less than or equal to x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
        # the high moved below the low: applies on e.g. sqrt(8)
        return high


s = Solution()
print(s.mySqrt(8))  # 2
print(s.mySqrt(100))  # 10
print(s.mySqrt(9))  # 3
