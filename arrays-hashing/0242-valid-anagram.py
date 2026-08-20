# 242. Valid Anagram: store counts of chars in separate hashmaps, compare counts afterward
# python does not use indexing for dicts
# Tell: order doesn't matter, only how many of each -> count into dicts ( anagram, permutation, rearrage, "can be formed from")


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        storedLetterFirst = {}
        storedLetterSecond = {}
        for i in range(len(s)):
            if s[i] in storedLetterFirst:
                storedLetterFirst[s[i]] += 1
            else:
                storedLetterFirst[s[i]] = 1
                 
        for i in range(len(t)):
            if t[i] in storedLetterSecond:
                storedLetterSecond[t[i]] += 1
            else:
                storedLetterSecond[t[i]] = 1

        
        for char in storedLetterFirst:
            if storedLetterFirst[char] != storedLetterSecond.get(char,0):
                return False
        return True       


        