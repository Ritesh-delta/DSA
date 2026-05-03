# ⚡ LeetCode 50 — Pow(x, n)

## 📌 Problem

Implement a function `pow(x, n)` to calculate **x raised to the power n (xⁿ)**.

---

## 🧠 My Approach

The first idea is brute force — multiply `x` repeatedly.
But that takes **O(n)** time, which is inefficient for large inputs.

Instead, I used **Binary Exponentiation (Fast Power)**:

* 🔹 If `n` is even → break it into half
* 🔹 If `n` is odd → reduce and multiply once more

This reduces the time complexity to **O(log n)**.

---

## ⚙️ Key Handling

* 🔸 Negative exponent → convert to `1 / xⁿ`
* 🔸 Base case → when `n = 0`, return `1`
* 🔸 Works efficiently for large values of `n`

---

## 📊 Complexity

* ⏱ Time: **O(log n)**
* 🧠 Space: **O(log n)** (recursion)

---

## 💡 What I Learned

* Optimizing brute force solutions
* Using divide & conquer techniques
* Handling edge cases properly

---

## 📝 Notes

This is a common interview problem and a good example of how a simple idea can be optimized significantly using the right approach.
