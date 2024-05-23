# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        dps = self.chk(1, root)

        return dps

        
    def chk(self, dps, node):
        lt = pow(10, 5)
        rt = pow(10, 5)
        if node.left == None and node.right == None:
            return dps
        if node.left != None:
            lt = self.chk(dps + 1, node.left)
        if node.right != None:
            rt =  self.chk(dps + 1, node.right)
        if lt < rt:
            return lt
        else:
            return rt