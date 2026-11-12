# Date: 12-11-2026
# Problem Number: 1281
# Problem Title: Subtract the Product and Sum of Digits of an Integer
# LeetCode Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(log N)
# Space Complexity: O(1)
    
    
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10

        return product - total