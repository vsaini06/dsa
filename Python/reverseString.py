class Solution():
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

sol = Solution()
s1 = ['h','e','l','l','o']
sol.reverseString(s1)
print(s1)

s2 = ['H','a','n','n','a','h']
sol.reverseString(s2)
print(s2)