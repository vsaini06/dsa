# DSA Python Prep

---

## Week 1: Arrays & Strings

### Pattern: HashMap / HashSet
#### [Two Sum](./Python/twosum.py)
- Store seen numbers in a hashmap, check if complement exists
- Time: O(n) | Space: O(n)
- Watch out: enumerate() → index first, value second

#### [Contains Duplicate](./Python/containsDuplicate.py)
- Store seen numbers in a set, return True if current number already exists
- Time: O(n) | Space: O(n)
- Watch out: use set() not {} for existence checks
- Pythonic shortcut: len(nums) != len(set(nums))

---

### Pattern: Sliding Window
#### [Best Time to Buy and Sell Stock](./Python/maxProfit.py)
- Track running min_price and max_profit in one pass
- profit = current_price - min_price_so_far
- Time: O(n) | Space: O(1)
- Watch out: min_price starts at float('inf') not 0

#### [Max Consecutive Ones III](./Python/maxConsecutive.py)
- Track zeros in window, shrink from left when zeros > k
- max_len = r - l + 1 after shrinking
- Time: O(n) | Space: O(1)
- Watch out: max_len update must be OUTSIDE the while loop

---

### Pattern: Two Pointers
#### [Move Zeroes](./Python/moveZeroes.py)
- l tracks next non-zero position, r scans entire array
- When r finds non-zero, swap with l, move l forward
- Time: O(n) | Space: O(1)
- Watch out: in-place modification, no return needed
- Python swap: nums[l], nums[r] = nums[r], nums[l]

#### [Container With Most Water](./Python/ContainerWithMostWater.py)
- Start with widest container (l=0, r=end), calculate area at every step
- Always move the shorter pointer inward
- area = (r - l) * min(heights[l], heights[r])
- Time: O(n) | Space: O(1)
- Watch out: compare heights not indices

#### [3Sum](./Python/3sum.py)
- Sort array, fix one number with i, use left/right pointers to find pair summing to -nums[i]
- If total < 0 → move left | If total > 0 → move right | If 0 → found triplet
- Skip duplicates: if nums[i] == nums[i-1] skip i
- Time: O(n²) | Space: O(1)
- Watch out: append as list [nums[i], nums[left], nums[right]]

---

### Pattern: Prefix Sum + HashMap
#### [Longest Subarray with Sum K](./Python/maxSubArray2.py)
- Use when: negatives in array (rules out sliding window)
- prefix_sum - k exists in seen → valid subarray found
- length = i - seen[prefix_sum - k]
- Initialize seen = {0: -1} to handle subarrays starting at index 0
- Time: O(n) | Space: O(n)
- Watch out: seen = {0: -1} not {0, -1} (dict not set)

---
---

## Week 2: Binary Search & Prefix Sum

### Pattern: Binary Search
#### [Binary Search](./Python/binarySearch.py)
- Variant 1: Classic - find exact target
- while left <= right, return mid or -1
- Time: O(log n) | Space: O(1)
- Watch out: left <= right not left < right

#### [Find Minimum in Rotated Sorted Array](./Python/minimumRotatedSorted.py)
- Variant 2: Left Boundary
- nums[mid] > nums[right] → left = mid+1 | else → right = mid
- while left < right, return nums[left]
- Time: O(log n) | Space: O(1)
- Watch out: right = mid not mid-1

#### [Search in Rotated Sorted Array](./Python/searchRotatedSortedArray.py)
- Variant 3: Modified Classic
- Check which half is sorted first, then check if target falls in it
- Left sorted if nums[left] <= nums[mid]
- Time: O(log n) | Space: O(1)

---

### Binary Search Master Guide
| Variant | Trigger | Loop | Right update | Return |
|---------|---------|------|--------------|--------|
| Classic | "find index" | left <= right | mid-1 | -1 |
| Left boundary | "find minimum" | left < right | mid | nums[left] |
| Search on answer | "minimum X such that" | left < right | mid | left |

**Watch-outs:**
- Always use left + (right-left)//2
- if/else is always O(1)
- right = mid when mid could be the answer

---

### Pattern: Kadane's Algorithm
#### [Maximum Subarray](./Python/maxSubArray.py)
- Reset currSum to 0 if negative, then add current element
- Initialize maxSum = nums[0] not 0
- Time: O(n) | Space: O(1)
- Watch out: all-negative arrays return least negative number

---

### Pattern: Prefix Sum
#### [Product of Array Except Self](./Python/productExceptSelf.py)
- Pass 1 (left→right): result[i] = product of all elements before i
- Pass 2 (right→left): result[i] *= product of all elements after i
- Store THEN update in both passes
- Time: O(n) | Space: O(1) extra

#### [Find Pivot Index](./Python/pivotIndex.py)
- right_sum = total - left_sum - nums[i]
- if left_sum == right_sum → return i
- Update left_sum AFTER the check
- Time: O(n) | Space: O(1)

#### [Running Sum of 1D Array](./Python/runningSum.py)
- running_sum[i] = running_sum[i-1] + nums[i]
- Initialize running_sum[0] = nums[0], loop from index 1
- Time: O(n) | Space: O(n)

---

### Pattern: Binary Search (Matrix)
#### [Search a 2D Matrix](./Python/searchMatrix.py)
- Treat matrix as flat sorted array of m*n elements
- flat index → row = mid // cols, col = mid % cols
- Classic binary search on range [0, rows*cols-1]
- Time: O(log(m*n)) | Space: O(1)
- Watch out: rows = len(matrix), cols = len(matrix[0])
- Matrix access: matrix[i][j] → i=row, j=col

---

## General Interview Tips
- Clarify: empty array? negatives? return value if no answer?
- State complexity BEFORE coding
- Dry run with a table
- Sliding window only works with non-negative numbers
- Prefix sum + hashmap for subarrays with negatives

## FAANG 5-Step Framework
1. Clarify constraints
2. State approach + complexity before coding
3. Code cleanly
4. Dry run out loud
5. State edge cases