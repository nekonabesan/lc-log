import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x0 = 5
        index = 100
        while index > 0:
            x0 = x0 - (((x0 ** 2) - x)/(2 * x0))
            index = index - 1

        result = int(math.floor(x0))
        return result -1
        