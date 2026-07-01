class Solution():
    def maxArea(self, heights):
        area, l, r = 0, 0, len(heights) - 1
        while l < r:
            area = max(area, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))