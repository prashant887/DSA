from typing import List

###
"""
From each index try to jump all possible indexes 
like at index 1 , val is 3 then 1+1,1+2,1+3  and capture what is the max index that can be jumped and try to jump the max
and at each point cal the max jump idx
"""
###

def canJump(nums: List[int]) -> bool:
    reachable=0
    for i in range(len(nums)):
        print(i,reachable,nums[i],i+nums[i])
        if i>reachable:
            #if current Index is greater than max possible reachable point
            return False
        reachable=max(reachable,i+nums[i])

    return True

#print(canJump( [2,3,1,1,4]))

print(canJump( [3,2,1,0,4]))