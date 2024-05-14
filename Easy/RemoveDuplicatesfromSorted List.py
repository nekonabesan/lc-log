# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        if head.next == None:
            return head

        result = head

        while head != None:
            if head.next != None:
                if head.val == head.next.val:
                    if head.next.next != None:
                        head.next = head.next.next
                        continue
                    else:
                        head.next = None
            head = head.next
                
        return result
            
