from typing import List


def removeElement( nums: List[int], val: int) -> int:
    i = 0
    n = len(nums)
    while i < n:

        if nums[i] == val:
            nums[i] = nums[n - 1]
            n = n - 1
        else:
            i=i+1

        print(nums)
        print(n)




nums = [3,2,2,3]
val = 3

removeElement(nums,val)
