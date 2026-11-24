# Date: 24-11-2026
# Problem Number: 1299
# Problem Title: Replace Elements with Greatest Element on Right Side
# LeetCode Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(maximum, temp)

        return arr