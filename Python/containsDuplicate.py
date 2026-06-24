class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for n in range(len(nums)):
            if nums[n] in seen:
                return True
            else:
                seen.add(nums[n])
        return False

sol = Solution()
print(sol.containsDuplicate([1,4,5,7,1,8]))
print(sol.containsDuplicate([2,5,7]))
print(sol.containsDuplicate([2,5,7,8,0,7]))