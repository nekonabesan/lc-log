class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chk = {}
        count = 0
        result = None
        for i in range(len(nums)):
            if nums[i] in chk.keys():
                chk[nums[i]] = chk[nums[i]] + 1
            else:
                chk[nums[i]] = 1

        keys = chk.keys()
        for i in range(len(keys)):
            if chk[keys[i]] > count:
                count = chk[keys[i]]
                result = keys[i]

        return result