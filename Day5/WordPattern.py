0/5

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        psmap = {}
        
        if len(pattern) != len(s_list):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in psmap:
                if s_list[i] not in psmap.values():
                    psmap[pattern[i]] = s_list[i]
                else:
                    return False
            else:
                if psmap[pattern[i]] != s_list[i]:
                    return False
        
        return True