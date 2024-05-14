class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dta = ''
        results = []

        count = len(digits) - 1
        intval = 0

        for i in range(len(digits)):
            intval = intval + (digits[i] * pow(10, count))
            count = count - 1

        intval = intval + 1
        dtaa = list(str(intval))

        for i in range(len(dtaa)):
            results.append(int(dtaa[i]))

        return results
        