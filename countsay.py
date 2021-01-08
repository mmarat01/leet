class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        dstring = self.countAndSay(n-1) # takes us to the Base Case; bottom-up
        dcount = 1 # starts at one as every string starts with 'new' first element
        i = 1 
        work = "" # parsing digit string to produce new one
        '''
        bounds are these as it allows for contiguous element checks; in the last run it will let us reach 
        the "else" case for the last sequence of elements (that was counted but not concatenated to new string)
        '''
        while i < len(dstring) + 1: 
            if i < len(dstring) and dstring[i] == dstring[i-1]: # same element as before? count it
                dcount += 1
            else:
                work += str(dcount) + dstring[i-1] # new element (or end of list)? add sequence that just ended
                dcount = 1
            i += 1
        return work

s = Solution()
print(s.countAndSay(4)) # "1211"
print(s.countAndSay(1)) # "1"
print(s.countAndSay(3)) # "21"
print(s.countAndSay(7)) # "13112221"