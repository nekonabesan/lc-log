class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        results = []
        line = []
        if numRows == 0:
            return results
        
        if numRows == 1:
            line.append(1)
            results.append(line)
            return results    
        
        for i in range(numRows):
            line = [1] * (i + 1)
            results.append(line)
        
        if numRows == 2:
            return results
        
        for i in range(len(results)):
            if i == 0 or i == 1:
                continue
            for j in range(len(results[i])):
                if j == 0:
                    continue
                elif j > (len(results[i]) - 2):
                    break
                results[i][j] = results[i - 1][j - 1] + results[i - 1][j]
            
        return results
        