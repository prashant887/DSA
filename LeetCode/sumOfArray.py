from typing import List


def add(one: List[int],two: List[int]) -> int:
    i=len(one)-1
    j=len(two)-1

    carry=0

    ans=[]

    while i>=0 and j >= 0:
        total=one[i]+two[j]+carry
        sm=total%10
        carry=total//10
        i=i-1
        j=j-1

        ans.insert(0,sm)

#if first array has more elements
    while i >= 0:
        total = one[i] + carry
        sm = total % 10
        carry = total // 10
        i = i - 1
        ans.insert(0, sm)

        # if first array has more elements
    while j >= 0:
        total = one[j] + carry
        sm = total % 10
        carry = total // 10
        j = j - 1
        ans.insert(0, sm)

    while carry != 0:
        total =  carry
        sm = total % 10
        carry = total // 10
        ans.insert(0, sm)

    print(ans)

    return 0

print(add([1 ,2, 3, 4],[6]))


