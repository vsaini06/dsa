class Solution:
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1


sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)
nums = [0, 1, 0, 3, 0, 9, 6, 51, 0]
sol.moveZeroes(nums)
print(nums)
nums = []
sol.moveZeroes(nums)
print(nums)