class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 0
        result = 0

        if len(prices) < 1:
            return max

        min = prices[0]

        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i] < min:
                # 安値更新
                min = prices[i]
            if result < (prices[i] - min):
                # 差益更新
                result = prices[i] - min

        return result