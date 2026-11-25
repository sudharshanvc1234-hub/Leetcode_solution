# Date: 25-11-2026
# Problem Number: 2032
# Problem Title: Two Out of Three
# LeetCode Link: https://leetcode.com/problems/two-out-of-three/
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        result = []

        for i in set(nums1):
            if i in nums2 or i in nums3:
                result.append(i)

        for i in set(nums2):
            if i in nums3:
                if i not in result:
                    result.append(i)

        return result