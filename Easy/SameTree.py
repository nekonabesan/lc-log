# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        result = True
        ap = []
        aq = []

        if p == None and q == None:
            return result
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False

        self.sch(p, ap)
        self.sch(q, aq)

        if len(ap) != len(aq):
            return False

        if p != None:
            self.sch(p.right, ap)
        if q != None:
            self.sch(q.right, aq)

        if len(ap) != len(aq):
            return False

        for i in range(len(ap)):
            if ap[i] != aq[i]:
                result = False
                break

        return result

    def sch(self, node, array):
        if node == None:
            return
        if node.left != None:
            self.sch(node.left, array)
        else:
            array.append(None)
        if node.right != None:
            self.sch(node.right, array)
        else:
            array.append(None)
        array.append(node.val)
        