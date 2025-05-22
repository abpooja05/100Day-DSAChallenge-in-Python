# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Count the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return head

        for _ in range(k):
            prev = None
            curr = head
            # Find last and second-last node
            while curr.next:
                prev = curr
                curr = curr.next
            # Rotate once
            prev.next = None
            curr.next = head
            head = curr

        return head
        