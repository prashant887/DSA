from typing import List


def plusOne(digits: List[int]) -> List[int]:
    add=1
    n = len(digits) - 1
    final = []
    while n>=0:
        added=add+digits[n]
        add=added//10
        sm=added%10
        final.insert(0,sm)
        n=n-1

    if add>0:
        final.insert(0,add)

    return final


digits = [1,2,3]
print(plusOne(digits))

digits = [4, 3, 2, 1]

print(plusOne(digits))

digits = [9]
print(plusOne(digits))
