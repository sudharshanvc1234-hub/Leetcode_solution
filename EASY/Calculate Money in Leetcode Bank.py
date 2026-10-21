# Date: 21-10-2026
# Problem Number: 1716
# Problem Title: Calculate Money in Leetcode Bank
# LeetCode Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
# Difficulty: Easy
# Topic: Array, Maths
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def totalMoney(self, n: int) -> int:
        save=[]
        for i in range(1,n+1):
            week = (i - 1) // 7
            day = (i - 1) % 7
            money = week + day + 1
            save.append(money)
        return sum(save)