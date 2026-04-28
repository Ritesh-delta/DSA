# 🔁 Leetcode 31. Next Permutation

## 🧩 Problem

Given an array of integers `nums`, rearrange it into the next lexicographically greater permutation.

If such an arrangement is not possible, rearrange it into the lowest possible order (i.e., sorted in ascending order).

The replacement must be **in-place** and use only **constant extra memory**.



## 📌 Examples

### Example 1
Input:
nums = [1,2,3]  
Output:
[1,3,2]

### Example 2
Input:
nums = [3,2,1]  
Output:
[1,2,3]

### Example 3
Input:
nums = [1,1,5]  
Output:
[1,5,1]

---

## 🧠 Approach

1. Traverse from right and find the first index `i` such that:
   nums[i] < nums[i + 1]

2. If such index exists:
   - Find the smallest number greater than nums[i] from the right
   - Swap them

3. Reverse the subarray from `i + 1` to end

4. If no such index exists:
   - Reverse the entire array

---
## 🎯 Key Insight

Find the first decreasing element from the right, swap it with the next greater element, then reverse the suffix to get the next permutation.

##  Tags

Array, Greedy, Two Pointers
