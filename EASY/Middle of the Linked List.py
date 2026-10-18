# Date: 18-10-2026
# Problem Number: 876
# Problem Title: Middle of the Linked List
# LeetCode Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
# Difficulty: Easy
# Topic: Linked List,2 Pointers
# Time Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow=head
        fast=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
        