from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)

    i=0
    j=k-1
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i=i+1
        j=j-1

    print(nums)

    i=k
    j=len(nums)-1



    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i=i+1
        j=j-1

    print(nums)

    i = 0
    j = len(nums) - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = j - 1

    print(nums)





"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

4 3 2 1  | 7 6 5
5 6 7 1 2 3 4
"""
nums = [-1,-100,3,99]

k = 2

rotate(nums,k)
print(nums)