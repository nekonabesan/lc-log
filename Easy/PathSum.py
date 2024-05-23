# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        results = []
        result = False
        self.chk(root, 0, results)

        for i in range(len(results)):
            if results[i] == targetSum:
                result = True
                break

        return result


    def chk(self, node, num, results):
        if node.left == None and node.right == None:
            results.append(num + node.val)
        if node.left != None:
            self.chk(node.left, num + node.val, results)
        if node.right != None:
            self.chk(node.right, num + node.val, results)
