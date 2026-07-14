# General notes Week 1

| Problem | Pattern | Status |
|---------|---------|--------|
| Two Sum | HashMap | ✓ |
| Best Time to Buy and Sell Stock | Sliding Window | ✓ |
| Contains Duplicate | Hash Set | ✓ |
| Move Zeroes | Two Pointers | ✓ |
| 3Sum | Sort + Two Pointers | ✓ |
| Container With Most Water | Two Pointers | ✓ |
| Longest Subarray with Sum K | Prefix Sum + HashMap | ✓ |
| Max Consecutive Ones III | Sliding Window | ✓ |

**Patterns learned:**
- HashMap / HashSet
- Two Pointers
- Sliding Window
- Prefix Sum

**Recurring watch-outs:**
- enumerate() → index first, value second
- Variable name consistency throughout
- max_len update outside while loops
- {0: -1} dict not {0, -1} set

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

## Max Consecutive Ones III
- Pattern: Sliding Window
- Track zeros in window, shrink from left when zeros > k
- max_len = r - l + 1 after shrinking
- Time: O(n) | Space: O(1)
- Watch out: max_len update must be OUTSIDE the while loop

## Binary Search (Week 2): Master Guide

### The 3 Key Decisions
1. Exact value or boundary?
2. Searching array or value range?
3. right = mid or mid - 1?

### Decision Framework
| Trigger phrase | Loop | Right update | Return |
|----------------|------|--------------|--------|
| "find index of target" | left <= right | mid - 1 | -1 |
| "find minimum/first" | left < right | mid | nums[left] |
| "find maximum/last" | left < right | mid | nums[left] |
| "find minimum X such that" | left < right | mid | left |

### Variant 1 — Classic (exact match)
- left <= right, return mid or -1
- right = mid - 1 when mid is NOT the answer

### Variant 2 — Left Boundary (find minimum)
- left < right, right = mid (mid could be answer)
- return nums[left] after loop

### Variant 3 — Modified (rotated array)
- Check which half is sorted first
- left sorted if nums[left] <= nums[mid]
- right sorted if nums[left] > nums[mid]
- Then check if target falls in sorted half

### Variant 4 — Search on Answer (value range)
- Not searching array, searching range of values
- left = min possible, right = max possible
- Trigger: "find minimum X such that condition is true"
- return left after loop

### Signal Words
- "find index" → Classic
- "find minimum in rotated" → Left boundary  
- "search in rotated" → Modified classic
- "minimum days/speed/capacity" → Search on answer

### Watch-outs
- Always use left + (right-left)//2 not (left+right)//2
- left <= right for exact match, left < right for boundary
- right = mid not mid-1 when mid could be the answer
- if/else is always O(1), doesn't affect loop complexity

## Binary Search (Classic)
- Pattern: Binary Search
- Sorted array, find exact target
- while left <= right, mid = left + (right-left)//2
- target > nums[mid] → left = mid+1 | target < nums[mid] → right = mid-1
- Time: O(log n) | Space: O(1)
- Watch out: left <= right not left < right, indentation inside while loop
- mid uses // (floor division), always rounds down

## Find Minimum in Rotated Sorted Array
- Pattern: Binary Search (modified)
- Compare nums[mid] with nums[right] to find which half has the drop
- nums[mid] > nums[right] → minimum on right → left = mid + 1
- nums[mid] < nums[right] → minimum on left including mid → right = mid
- Loop condition: while left < right (not <=)
- Return nums[left] after loop
- Time: O(log n) | Space: O(1)
- Watch out: right = mid not mid-1, use left < right not left <= right

## Search in Rotated Sorted Array
- Pattern: Binary Search (modified)
- One half is always sorted — figure out which, then check if target is in it
- Left sorted if nums[left] <= nums[mid]
  - target in [nums[left], nums[mid]) → right = mid - 1
  - else → left = mid + 1
- Right sorted if nums[left] > nums[mid]
  - target in (nums[mid], nums[right]] → left = mid + 1
  - else → right = mid - 1
- Time: O(log n) | Space: O(1)
- Watch out: use left <= right, return -1 after loop

## Maximum Subarray (Kadane's Algorithm)
- Pattern: Kadane's Algorithm (dynamic programming lite)
- At each element: reset currSum to 0 if negative, then add current element
- currSum = max(currSum, 0) then currSum += n
- Track maxSum throughout, initialize to nums[0] not 0
- Time: O(n) | Space: O(1)
- Watch out: initialize maxSum = nums[0] not 0, handles all-negative arrays
- Key insight: if current subarray is dragging you down, start fresh

## General Reminders
- Clarify: empty array? single element? return value if no answer?
- State complexity BEFORE coding
- Dry run with a table
- Edge cases: empty, single element, no valid answer
