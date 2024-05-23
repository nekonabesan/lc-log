# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None:
            return None
        if len(nums) == 0:
            return None
        return self.create(nums)

    def create(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.create(nums[:mid])
        if mid < len(nums)-1:
            node.right = self.create(nums[mid+1:])
        return node