# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False

        return self.test(root.left, root.right)
        
    def test(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        if (left.val == right.val) and ((self.test(left.left, right.right) == True)
            and (self.test(left.right, right.left) == True)):
            return True
        else:
            return False