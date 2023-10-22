from typing import List


def twoSum( numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i<j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] > target:
            j = j - 1
        else:
            i = i + 1


numbers = [2,7,11,15]
target = 9

print(twoSum(numbers,target))

numbers = [2,3,4]
target = 6
print(twoSum(numbers,target))

numbers = [-1,0]
target = -1
print(twoSum(numbers,target))

