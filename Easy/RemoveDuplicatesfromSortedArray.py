class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        buf = []
        index = 0
        length = len(nums)
        while index < length:
            chk = nums[index] in buf
            if chk == True:
                nums.pop(index)
                length = len(nums)
            else:
                buf.append(nums[index])
                index = index + 1
        
        