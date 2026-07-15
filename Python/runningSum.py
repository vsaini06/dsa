class Solution():
    def runningSum(self, nums):
        n = len(nums)
        running_sum = [0] * n
        running_sum[0] = nums[0]
        for i in range(1, n):
            running_sum[i] = running_sum[i - 1] + nums[i]
        return running_sum

sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
print(sol.runningSum([1, 1, 1, 1, 1]))
print(sol.runningSum([3, 1, 2, 10, 1]))