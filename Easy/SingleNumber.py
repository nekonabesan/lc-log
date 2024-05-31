class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = {}
        result = None

        for i in range(len(nums)):
            if nums[i] not in arr:
                arr[nums[i]] = 1
            else:
                arr[nums[i]] = arr[nums[i]] + 1

        for k in arr.keys():
            if arr[k] == 1:
                result = k
                break
        
        return result