class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        output = 0

        if len(nums) == 1:
            if nums[0] < target:
                return 1
            elif nums[0] > target:
                return output
            elif nums[0] == target:
                return output

        for i in range(len(nums)):
            if i == 0:
                if target <= nums[i]:
                    output = 0
                    break
                else:
                    continue
            else:
                if nums[i - 1] < target and target <= nums[i]:
                    output = i
                    break
            if i == (len(nums) - 1):
                output = i + 1
                break
        
        return output