# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Create an empty node to handle first scenario where head is null
        head = ListNode()
        
        #Our output linked list
        p = head
        
        #Itearate all nodes in l1 and l2 and find the one with lesser value and append to output list
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
        
        #If l2 list is fully iterated but l1 list is still left, we can directly attach it to output
        if l1:
            p.next = l1
        #If l1 list is fully iterated but l2 list is still left, we can directly attach it to output
        elif l2:
            p.next = l2
        
        #Return the ouput list omitting the empty node we attached at beginning
        return head.next