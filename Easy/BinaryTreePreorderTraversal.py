# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []

        if root == None:
            return results

        self.chk(root, results)

        return results

    def chk(self, node, results):
        if node == None:
            return
        results.append(node.val)
        if node.left != None:
            self.chk(node.left, results)
        if node.right != None:
            self.chk(node.right, results)