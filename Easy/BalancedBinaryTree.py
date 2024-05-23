# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        
        dps = self.chk(0, root)

        if dps == -1:
            return False
        else:
            return True

    def chk(self, dps, node):
        lt = dps
        rt = dps
        if node == None:
            return dps
        if node.left != None:
            lt = self.chk(dps + 1, node.left)
        if node.right != None:
            rt = self.chk(dps + 1, node.right)
        if lt == -1 or rt == -1 or abs(lt - rt) > 1:
            return -1
        if lt > rt:
            return lt
        else:
            return rt