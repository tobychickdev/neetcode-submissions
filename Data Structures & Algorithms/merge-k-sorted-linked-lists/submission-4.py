# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        else:
            working_list = lists[0]
        for i in range(1, len(lists)):
            working_list = self.merge2Lists(working_list, lists[i])
            temp = working_list
        return working_list

    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while list1 or list2:
            if not list1:
                while list2:
                    head.next = list2
                    head = head.next
                    list2 = list2.next
                break;
            if not list2:
                while list1:
                    head.next = list1
                    head = head.next
                    list1 = list1.next
                break;

            v1 = list1.val
            v2 = list2.val
            if v1 <= v2:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = None
        return dummy.next



        
        