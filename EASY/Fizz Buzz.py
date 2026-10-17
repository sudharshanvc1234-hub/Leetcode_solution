# Date: 17-10-2026
# Problem Number: 412
# Problem Title: Fizz Buzz
# LeetCode Link: https://leetcode.com/problems/fizz-buzz/description/
# Difficulty: Easy
# Topic: List, String
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result