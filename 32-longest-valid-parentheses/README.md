# 🔁 Leetcode 32.Longest Valid Parentheses

🧩 Problem
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

📌 Examples

Example 1
Input: s = "(()"
Output: 2

Example 2
Input: s = ")()())"
Output: 4

Example 3
Input: s = ""
Output: 0

🧠 Approach
Use a stack to store indices

Initialize stack with -1 (base index)

Traverse the string:
- If '(' → push index into stack
- If ')' → pop from stack
  - If stack becomes empty → push current index (reset base)
  - Else → calculate length using: current index - top of stack

Keep updating maximum length

🎯 Key Insight
Store indices instead of characters and use a base index to calculate the length of valid substrings.

Tags
Stack, String, Dynamic Programming
