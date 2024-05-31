# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        result = False

        if head == None:
            return False

        while head != None:
            # listを使う場合とdict使う場合で時間/領域計算量がトレードオフ
            if head not in arr:
                arr.append(head)
            else:
                result = True
                break
            head = head.next
        
        return result
