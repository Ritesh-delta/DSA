# 🧩 LeetCode 62 — Unique Paths

## 📌 Problem Statement

A robot is placed at the **top-left corner** of an `m x n` grid 🤖.  
It can only move in two directions:

➡️ Right  
⬇️ Down  

The goal is to reach the **bottom-right corner** of the grid.

👉 You need to find the total number of **unique paths** possible.

---

## 🧪 Example

### Example 1

Input: m = 3, n = 7
Output: 28


### Example 2

Input: m = 3, n = 2
Output: 3


📌 Explanation:  
The robot can take different combinations of right and down moves to reach the destination.

---

## 💡 Idea / Approach

### 🧠 Dynamic Programming

Each cell in the grid represents:

👉 Number of ways to reach that cell

We build the answer step by step:

- First row → only 1 way (move right ➡️)
- First column → only 1 way (move down ⬇️)
- Other cells → sum of top + left cells

---

## 🔄 Key Insight

To reach any cell:
- From above ⬆️
- From left ⬅️  

So:

👉 Total ways = top + left

---

## ⚡ Optimized Approach

Instead of using a full grid, we can reduce space using a single row array and update values iteratively.

---

## 🧮 Mathematical Insight

This problem can also be solved using combinatorics:

- Total moves = `(m - 1) + (n - 1)`
- Choose positions of down (or right) moves

👉 It becomes a combinations problem

---

## ⏱ Complexity

- Time Complexity: `O(m × n)`
- Space Complexity:
  - `O(m × n)` (basic DP)
  - `O(n)` (optimized DP)

---

## 🎯 What I Learned

✔ Grid-based DP patterns  
✔ Optimizing space complexity  
✔ Connection between DP and combinatorics  

---

## 🏷️ Tags

`#DynamicProgramming` `#Math` `#GridProblems` `#Combinatorics`

---
