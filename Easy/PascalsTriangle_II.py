class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        results = []
        line = []
        
        for i in range(rowIndex + 1):
            line = [1] * (i + 1)
            if i == 0:
                results.append(line)
                continue
            if i == 1:
                results.append(line)
                continue
            results.append(line)
            for j in range(len(results[i])):
                if j == 0:
                    continue
                elif j > (len(results[i]) - 2):
                    break
                results[i][j] = results[i - 1][j - 1] + results[i - 1][j]
            
        return results[rowIndex]