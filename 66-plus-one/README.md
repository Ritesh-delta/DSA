# ➕ LeetCode 66 — Plus One

## 📌 Problem

You are given a number represented as an array of digits.

- Each element in the array represents a single digit 🧮  
- Digits are stored in **left-to-right order** (most significant first)  
- The number has **no leading zeros**

👉 Your task is to **add one to the number** and return the updated array.

---

## 🧪 Examples

### Example 1

Input: digits = [1,2,3]
Output: [1,2,4]


### Example 2

Input: digits = [4,3,2,1]
Output: [4,3,2,2]


### Example 3

Input: digits = [9]
Output: [1,0]


📌 Explanation:  
When the last digit becomes `10`, we carry over just like normal addition.

---

## 💡 Approach

### 🧠 Idea

Start from the **last digit** and simulate addition:

- If digit < 9 → just add 1 and stop ✅  
- If digit == 9 → make it 0 and carry forward 🔁  

Keep moving left until:
- Carry stops, OR
- You finish the entire array

---

## 🔄 Edge Case

If all digits are `9` (like `[9,9,9]`):

➡️ Result becomes `[1,0,0,0]`

---

## ⚡ Key Insight

This problem is just **basic addition with carry**, but done on an array instead of a number.

---

## ⏱ Complexity

- Time Complexity: `O(n)`  
- Space Complexity: `O(1)` (ignoring output array)

---

## 🎯 What I Learned

✔ Handling carry in arrays  
✔ Edge cases (all 9’s case)  
✔ Thinking beyond direct integer conversion  

---

## 🏷️ Tags

`#Array` `#Math` `#Simulation`

---

⭐ Simple problem, but very important for building fundamentals!
