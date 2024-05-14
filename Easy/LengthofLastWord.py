class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = s.split(' ')
        result = 0

        if len(strs) == 0:
            return result

        for i in range(len(strs)):
            length = len(list(strs[i]))
            if length > 0:
                result = length

        return result

