# 🧩 35. Search Insert Position

## 📌 Problem  
Given a sorted array of distinct integers and a target value, return the index if the target is found.  
If not, return the index where it would be inserted in order.

---

## 💡 Idea  

Since the array is sorted and we need O(log n), brute force is not a good option ❌  

So the idea is to use **Binary Search**:

- Compare middle element with target  
- Move left or right accordingly  
- If not found, return the correct insert position  

---

## ⚙️ Approach  

- Initialize `left = 0` and `right = len(nums) - 1`  
- Find mid index  
- If `nums[mid] == target` → return mid  
- If `nums[mid] < target` → move to right half  
- Else → move to left half  
- When loop ends, `left` will be the correct insert position  

---

## 🔑 Key Point  

Even if the target is not present,  
👉 the `left` pointer always ends at the correct insert position.

---

## 🧪 Example  

**Input:**
