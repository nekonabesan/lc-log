class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        tmp = None
        carry = 0
        result = []

        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp

        len_a = len(a) - 1
        len_b = len(b) - 1
        index_a = len_a
        index_b = len_b
        
        while index_a >= 0:
            if index_b >= 0:
                test = int(carry) + (int(a[index_a], 2) + int(b[index_b], 2))
                if test % 2 == 0:
                    binval = 0
                else:
                    binval = 1
                if int(carry) & int(a[index_a], 2) == 1:
                    carry = 1
                elif int(carry) & int(b[index_b], 2) == 1:
                    carry = 1
                elif int(a[index_a], 2) & int(b[index_b], 2) == 1:
                    carry = 1
                else:
                    carry = 0
            else:
                test = int(carry) + int(a[index_a], 2)
                if test % 2 == 0:
                    binval = 0
                else:
                    binval = 1
                if int(carry) & int(a[index_a], 2) == 1:
                    carry = 1
                else:
                    carry = 0
            result.insert(0, binval)
            index_a = index_a - 1
            index_b = index_b - 1

        if carry > 0:
            result.insert(0, carry)

        return ''.join(map(str, result))