# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head:
            return None

        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals.sort()

        curr = head
        i = 0

        while curr:
            curr.val = vals[i]
            i += 1
            curr = curr.next

        return head