def trim(s: str)->str:
    i=0
    j=len(s)-1
    s=list(s)
    while i<j and s[j]==' ':
        j=j-1

    while i<j and s[i]==' ':
        i=i+1

    ss=s[i:j+1]

    i = 0
    j = len(ss) - 1
    while i<j:
        ss[i],ss[j]=ss[j],ss[i]
        i=i+1
        j=j-1

    print(ss)

    return ''.join(ss)

trim("  hello  world  ")