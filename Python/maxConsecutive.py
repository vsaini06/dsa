class Solution():
    def maxConsecutive(self, nums, k):
        left, max_len, zeros = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


sol = Solution()
print(sol.maxConsecutive([1,1,0,0,0,1,1], 2))
print(sol.maxConsecutive([1,1,1,0,0,0,1,1,1,1,0], 2))
print(sol.maxConsecutive([0,0,0], 0))