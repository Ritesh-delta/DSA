# Remove Element — LeetCode 27

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.  
Return the number of elements `k` such that the first `k` elements of `nums` contain values not equal to `val`.

. The order of elements does not matter  
. Elements beyond the first `k` are ignored

##  Approach — Two Pointers

We use a two-pointer technique:

. `i` → iterates through the array  
. `k` → tracks position for valid elements

**Steps:**
1. Initialize `k = 0`
2. Loop through the array:
   - If `nums[i] != val`, place it at `nums[k]` and increment `k`
3. Return `k`



# 🚀 Key Insight

Instead of deleting elements (which is O(n) per deletion), we **overwrite** unwanted values using a write pointer `k`. Only the first `k` elements of the result matter — everything beyond is ignored.
