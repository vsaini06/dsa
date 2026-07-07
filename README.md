## Two Sum
- Pattern: Hash Map
- Store seen numbers in a hashmap, check if complement exists
- Time: O(n) | Space: O(n)
- Watch out: enumerate() → index first, value second

## Best Time to Buy and Sell Stock
- Pattern: Sliding Window
- Track running min_price and max_profit in one pass
- profit = current_price - min_price_so_far
- Time: O(n) | Space: O(1)
- Watch out: min_price starts at float('inf'), not 0

## Contains Duplicate
- Pattern: Hash Set
- Store seen numbers in a set, return True if current number already exists
- Time: O(n) | Space: O(n)
- Watch out: use set() not {} for existence checks, no need to store index
- Pythonic shortcut: len(nums) != len(set(nums))

## Move Zeroes
- Pattern: Two Pointers
- l tracks next non-zero position, r scans entire array
- When r finds non-zero, swap with l, move l forward
- Time: O(n) | Space: O(1)
- Watch out: in-place modification, no return needed
- Python swap: nums[l], nums[r] = nums[r], nums[l]

## 3Sum
- Pattern: Sort + Two Pointers
- Sort array, fix one number with i, use left/right pointers to find pair summing to -nums[i]
- If total < 0 → move left right | If total > 0 → move right left | If 0 → found triplet
- Skip duplicates: if nums[i] == nums[i-1] skip i | after finding triplet skip duplicate left/right values
- Time: O(n²) | Space: O(1)
- Watch out: method name is threeSum not 3sum, append as a list [nums[i], nums[left], nums[right]]

## Container With Most Water
- Pattern: Two Pointers
- Start with widest container (l=0, r=end), calculate area at every step
- Always move the shorter pointer inward (chance of finding taller line)
- area = (r - l) * min(heights[l], heights[r])
- Time: O(n) | Space: O(1)
- Watch out: compare heights not indices when deciding which pointer to move

## Longest Subarray with Sum K
- Pattern: Prefix Sum + Hashmap
- Use when: negatives in array (rules out sliding window)
- prefix_sum - k exists in seen → valid subarray found
- length = i - seen[prefix_sum - k]
- Initialize seen = {0: -1} to handle subarrays starting at index 0
- Only store first occurrence of each prefix_sum (for maximum length)
- Time: O(n) | Space: O(n)
- Watch out: seen = {0: -1} not {0, -1} (dict not set)

## General Reminders
- Clarify: empty array? single element? return value if no answer?
- State complexity BEFORE coding
- Dry run with a table
- Edge cases: empty, single element, no valid answer
