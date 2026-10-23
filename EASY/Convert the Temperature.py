# Date: 23-10-2026
# Problem Number: 2469
# Problem Title: Convert the Temperature
# LeetCode Link: https://leetcode.com/problems/convert-the-temperature/description/
# Difficulty: Easy
# Topic: Array, Append Operator
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans=[]
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        ans.append(kelvin)
        ans.append(Fahrenheit)
        return ans 