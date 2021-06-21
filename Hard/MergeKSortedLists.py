# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge2Lists(l1, l2):
            dummy = ListNode()
            p = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists)>1:
            new_list = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None 
                new_list.append(merge2Lists(l1,l2))
            lists = new_list
                
        return lists[0]
        

            
        