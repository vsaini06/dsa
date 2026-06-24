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

## General Reminders
- Clarify: empty array? single element? return value if no answer?
- State complexity BEFORE coding
- Dry run with a table
- Edge cases: empty, single element, no valid answer
