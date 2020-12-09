class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: # empty list
            return ""
        if len(strs) == 1: # only one string
            return strs[0]
        
        # assume first string is prefix
        pref = strs[0]
        plen = len(strs[0])
        
        for s in strs[1:]: # for all strings, 2nd onwards
            while pref != s[0:plen]: # while pref we assumed is too big (high expectations), shorten it until it matches prefix in current word
                plen -= 1 
                pref = pref[0:plen] 
                if plen == 0: # basically no match at all
                    return ""
        
        return pref
                