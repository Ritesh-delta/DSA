🧩 43. Multiply Strings
📌 Problem

Given two numbers in string format, return their product as a string without converting them to integers.

💡 Idea

At first, I thought of converting the strings to integers, but that’s not allowed ❌

So I treated it like normal multiplication we do on paper:

Multiply digit by digit
Keep track of positions
Handle carry carefully
⚙️ Approach
Create a result array of size n + m
Traverse both strings from right to left
Multiply digits and add to correct position
Store carry and remainder properly
Convert final result to string and remove leading zeros
🔑 Key Point

If we multiply digits at index i and j, their result contributes to:

Current position
Carry goes to previous position

👉 This index mapping is the main trick.

🧪 Example

Input:

num1 = "123"
num2 = "456"

Output:

"56088"
⏱️ Complexity
Time: O(n * m)
Space: O(n + m)
📚 What I Learned
How to simulate multiplication without integers
Working with strings and arrays together
Importance of index handling and carry
📝 Notes
Edge case: if any number is "0" → return "0"
Remove leading zeros in final result
