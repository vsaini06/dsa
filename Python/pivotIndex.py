class Solution():
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum, right_sum = 0, 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
print(sol.pivotIndex([1, 2, 3]))
print(sol.pivotIndex([-1, -1, -1, 0, 1, 1]))
print(sol.pivotIndex([]))