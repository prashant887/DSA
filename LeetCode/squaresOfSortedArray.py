from typing import List


def sortedSquares( nums: List[int]) -> List[int]:
    new_list = list(map(lambda x:x*x,nums))

    return sorted(new_list)


nums = [-4,-1,0,3,10]

print(sortedSquares(nums))