class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        length = len(nums)
        while index < length:
            if nums[index] == val:
                nums.pop(index)
                length = len(nums)
            else:
                index = index + 1
        