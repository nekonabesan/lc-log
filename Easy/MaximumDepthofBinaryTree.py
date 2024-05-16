# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        l = self.dfs(root.left, 1)
        r = self.dfs(root.right, 1)

        if r > l:
            return r
        else:
            return l

    def dfs(self, node, num):
        r = num
        l = num
        if node == None:
            return num
        if node.left != None:
            r = self.dfs(node.left, num + 1)
        else:
            r = r + 1
        if node.right != None:
            l = self.dfs(node.right, num + 1)
        else:
            l = l + 1

        if r > l:
            return r
        else:
            return l