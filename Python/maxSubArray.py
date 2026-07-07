class Solution():
    def maxSubArray(self, nums, k):
        prefix_sum, max_length = 0, 0
        seen = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in seen:
                max_length = max(max_length, i - seen[prefix_sum - k])
            if prefix_sum not in seen:
                seen[prefix_sum] = i
        return max_length

sol = Solution()
print(sol.maxSubArray([1, 2, 3, 1, 1, 1], 3))
print(sol.maxSubArray([1, -1, 1, 1, 1, 1], 3))
print(sol.maxSubArray([1, 2, 3], 6))
print(sol.maxSubArray([1, 2, 3], 10))
