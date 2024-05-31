import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = True

        if s == " ":
            return True

        s = re.sub("[^a-zA-Z0-9]+", "", s)
        strs = list(s.lower())
        if len(strs) == 0:
            return True
        
        j = len(strs) - 1
        for i in range(len(strs)):
            if strs[i] != strs[j]:
                result = False
            j = j - 1

        return result