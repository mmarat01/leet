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
        pairs = {")": "(", "}": "{", "]": "["}
        for val in s:
            if val in pairs:  # we have a closing
                if (
                    stack and stack[-1] == pairs[val]
                ):  # not empty and last one matches current closing
                    stack.pop()
                else:
                    return False  # either it was empty when it shouldn't (current was closing) or wasn't empty but no match
            else:
                stack.append(val)  # current is opening
        return not stack  # true if empty (all pairs matched)


"""
    Reviewed on February 26, 2021:
        Algorithm goes like:
            Traverse string.
            If current value is an opening bracket, then push it to the stack.
            The stack's last-in-first-out logic helps because in a valid string, the last opening bracket is the one that must be
            matched with a closing.
            If current value is a closing bracket, we need to peak at the top of the stack (aka last added opening bracket).
                If the stack is empty or the stack's top is not the appropriate opening for the current closing, we return false.
            We return true if the stack is empty (given all pairs were succesfully matched).
                Easy to represent as "return not stack" -- true if empty, false if not empty.
    """
s = Solution()
print(s.isValid("()"))  # true
print(s.isValid("()[]{}"))  # true
print(s.isValid("(]"))  # false
print(s.isValid("([)])"))  # false
print(s.isValid("((()()))"))  # true
print(s.isValid("((()"))  # false
