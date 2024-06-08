# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        result = None

        arr = {}

        if headA == None or headB == None:
            return None

        while headA != None:
            arr[id(headA)] = headA.val
            headA = headA.next

        while headB != None:
            if id(headB) in arr:
                result = headB
                break
            headB = headB.next

        return result