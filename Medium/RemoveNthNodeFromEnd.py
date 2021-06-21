# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #Start 2 pointers at beginning
        
        fast, slow = head,head
        
        
        #Give the fast pointer a head-start :: Move it by n positions
        for i in range(n):
            fast = fast.next
            
        #To handle scenarios where there is just one node
        if not fast:
            return head.next
        
        #Move both pointers till fast pointer is at last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #Now slow is at one position less than the node to delete
        slow.next = slow.next.next
        return head