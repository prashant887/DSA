from typing import List


def roated(nums: List[int]) -> int:
    i=0
    if nums[0]<nums[len(nums)-1]:
        return 0

    while nums[i]>nums[len(nums)-1]:
        i=i+1

    return i

print(roated([3,4,5,1,2]))

print(roated([1,2,3,4,5]))

print(roated([4,5,1,2,3]))