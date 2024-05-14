class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        output = -1
        h = list(haystack)
        n = list(needle)

        if len(n) > len(h):
            return output

        if len(n) == 0 or len(h) == 0:
            return output

        for i in range(len(h)):
            flg = True
            if len(n) > (len(h) - i):
                break
            for j in range(len(n)):
                if h[i + j] != n[j]:
                    flg = False
                    break
            if flg == True:
                output = i
                break
        return output

        