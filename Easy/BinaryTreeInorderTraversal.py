# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result


        self.sch(root, result)

        return result

    def sch(self, node, result):
        if node.left != None:
            self.sch(node.left, result)
        if node.val != None:
            result.append(node.val)
        if node.right != None:
            self.sch(node.right, result)
        