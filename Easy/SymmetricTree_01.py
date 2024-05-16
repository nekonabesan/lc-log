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
        result = True
        al = []
        ar = []

        if root == None:
            return False
        
        self.sch1(root.left, al)
        self.sch2(root.right, ar)

        if len(al) != len(ar):
            return False
        
        j = len(ar) - 1
        for i in range(len(ar)):
            if ar[i] != al[j]:
                result = False
            j = j - 1
        
        return result

    def sch1(self, node, array):
        if node == None:
            return
        if node.left != None:
            self.sch1(node.left, array)
        else:
            array.append(9998)
        if node.right != None:
            self.sch2(node.right, array)
        else:
            array.append(9999)
        array.append(node.val)

    def sch2(self, node, array):
        if node == None:
            return
        array.append(node.val)
        if node.left != None:
            self.sch1(node.left, array)
        else:
            array.append(9999)
        if node.right != None:
            self.sch2(node.right, array)
        else:
            array.append(9998)