# Date: 30-10-2026
# Problem Number: 2520
# Problem Title: Count the Digits That Divide a Number
# LeetCode Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(D)
# Space Complexity: O(D)
#Here, D = number of digits.

class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        for digit in str(num):
            val=int(digit)

            if num%val==0:
                count+=1
        return count

