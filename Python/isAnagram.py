class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))
print(sol.isAnagram("", ""))
print(sol.isAnagram("a", "a"))
print(sol.isAnagram("ab", "a"))