# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # empty needles are zeroes
            return 0
            
        if needle in haystack: 
            for i in range(len(haystack)): 
                if haystack[i] == needle[0]: # find first character of needle
                    if haystack[i:i+len(needle)] == needle: # chop haystack starting at current pos to length of needle, if equal, that's it
                        return i
        
        return -1
s = Solution()
print(s.strStr("hello", "ll")) # 2
print(s.strStr("aaaaaa", "bba")) # -1
print(s.strStr("asdf", "")) # 0
print(s.strStr("yeportpop", "pop")) # 6
print(s.strStr("", "abc")) # -1