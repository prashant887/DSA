from typing import List

###
"""
From each index try to jump all possible indexes 
like at index 1 , val is 3 then 1+1,1+2,1+3  and capture what is the max index that can be jumped and try to jump the max
and at each point cal the max jump idx

Greedy Algo go for max value idx jump
"""
###

def jumpSolution(nums: List[int]) -> int:
    """

    Search between each windown
    :param nums:
    :return:
    """
    l=0
    r=0
    res = 0

    while r<len(nums)-1:
        farherst=0
        #search the current window
        for i in range(l,r+1):
            farherst=max(farherst,i+nums[i])
        l=r+1
        r=farherst
        res=res+1

    return res

def canJump(nums: List[int]) -> int:
    reachable=0
    jumpIndex=0
    totalJumps=0
    dest=len(nums)-1

    if dest == 0:
        return 0
    
    for i in range(len(nums)):
        reachable=max(reachable,i+nums[i])
        print(i,nums[i],reachable,nums[reachable])

        """
            This points the end of current window so jumped there
            [2,3,1,1,4]
            from 2 to jump 1 or jump to 3 , max val jum pos 0+val at 0
            that makes 1 jump to idx 2 (val 1) , now 
            till i reached current jump idx in ssame window and not jumped
            whe i has reached max jum/boundery do next jump from next
            
            i==jumpIndex reached end of current window do next jump
        """

        if i==jumpIndex:
            print(" jumpIdx ",i,jumpIndex,reachable)
            jumpIndex=reachable
            totalJumps=totalJumps+1

            #if coverage is reached end
            if reachable>=dest:
                return totalJumps


#print(canJump( [2,3,1,1,4]))
"""
print(jumpSolution(nums = [2,3,1,1,4]))
print(canJump(nums = [2,3,1,1,4]))

print("\n")

print(jumpSolution(nums = [2,3,0,1,4]))
print(canJump(nums = [2,3,0,1,4]))
"""

print(canJump(nums = [2,3,1,1,4]))
