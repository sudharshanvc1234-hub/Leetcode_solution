# Date: 05-11-2026
# Problem Number: 1431
# Problem Title:  Kids With the Greatest Number of Candies
# LeetCode Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
# Difficulty: Easy
# Topic: Array, For loops 
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output=[]
        highest=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=highest:
                output.append(True)
            else:
                output.append(False)
        return output
