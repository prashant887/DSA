from typing import List


def maxProfit( prices: List[int]) -> int:
    minSoFar=prices[0]
    maxSoFar=0
    for i in prices:
        minSoFar=min(minSoFar,i)
        diff=i-minSoFar
        maxSoFar=max(maxSoFar,diff)

    return maxSoFar

def maxProfitBuySell(prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res = res + (prices[i] - prices[i - 1])

        return res

print(maxProfit([7,6,4,3,1]))
