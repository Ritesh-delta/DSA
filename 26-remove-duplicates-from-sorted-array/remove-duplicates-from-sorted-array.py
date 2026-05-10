class Solution:
    def removeDuplicates(self, nums):
        # Edge case: empty array
        if not nums:
            return 0

        # Pointer for the position of unique elements
        k = 1

        # Start from the second element
        for i in range(1, len(nums)):
            # If current element is different from previous
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k