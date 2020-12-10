# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
# if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for val in s:
            if val in pairs: # we have a closing 
                if stack and stack[-1] == pairs[val]:#not empty and last one matches current closing
                    stack.pop() 
                else:
                    return False # either it was empty when it shouldn't (current was closing) or wasn't empty but no match
            else:
                stack.append(val) # current is opening
        return not stack #true if empty (all pairs matched)
        
s = Solution()
print(s.isValid('()')) # true
print(s.isValid('()[]{}')) # true
print(s.isValid('(]')) # false
print(s.isValid('([)])')) # false
print(s.isValid('((()()))')) # true
print(s.isValid('((()')) # false