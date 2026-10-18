# Date: 18-10-2026
# Problem Number: 1672
# Problem Title: Richest Customer Wealth
# LeetCode Link: https://leetcode.com/problems/richest-customer-wealth/description/
# Difficulty: Easy
# Topic: Array, Matrix
# Time Complexity: O(M*N)
# Space Complexity: O(1)
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        high_wealth=0
        for customers in accounts:
            if sum(customers)>high_wealth:
                high_wealth=sum(customers)
        return high_wealth
        
        