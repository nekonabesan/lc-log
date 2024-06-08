class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        n = columnNumber
        b = columnNumber
        a = 0
        dic = {
            0: 'Z'
            ,1: 'A'
            ,2: 'B'
            ,3: 'C'
            ,4: 'D'
            ,5: 'E'
            ,6: 'F'
            ,7: 'G'
            ,8: 'H'
            ,9: 'I'
            ,10: 'J'
            ,11: 'K'
            ,12: 'L'
            ,13: 'M'
            ,14: 'N'
            ,15: 'O'
            ,16: 'P'
            ,17: 'Q'
            ,18: 'R'
            ,19: 'S'
            ,20: 'T'
            ,21: 'U'
            ,22: 'V'
            ,23: 'W'
            ,24: 'X'
            ,25: 'Y'
        }
        result = []

        if n < 26:
            return dic[n]
        if n == 26:
            return dic[0]

        while n > 0:
            a = n  % 26
            result.insert(0, dic[a])
            n = (n - 1) // 26

        return ''.join(result)