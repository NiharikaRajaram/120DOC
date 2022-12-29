class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == None or t == None or len(s) == 0 or len(t) == 0 or len(s) != len(t):
            return False
            
        # two hashmaps
        sMap = {}
        tMap = {}

        # iterate parallely through both strings
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            
        # map sChar and tChar
            if sChar not in sMap:
                sMap[sChar] = tChar
            if tChar not in tMap:
                tMap[tChar] = sChar
            
        # if mappings do not match, return false
            if sMap[sChar] != tChar or tMap[tChar] != sChar:
                return False
        
        return True