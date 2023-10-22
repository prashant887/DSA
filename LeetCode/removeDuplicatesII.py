from typing import List


def removeDuplicates( nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    currentIndex = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[currentIndex - 2]:
            nums[currentIndex] = nums[i]
            currentIndex += 1

    return currentIndex


nums = [1,1,1,2,2,3]

print(removeDuplicates(nums))