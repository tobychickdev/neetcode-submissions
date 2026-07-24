# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #reverse
        prev = None
        start = head
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        reverse = prev

        # Reverse again and remove node
        k = 1
        prev = None
        while reverse:
            if k == n:
                print("reached here")
                reverse = reverse.next                
            else:
                temp = reverse.next
                reverse.next = prev
                prev = reverse
                reverse = temp
            k += 1
        new_head = prev

        return new_head






