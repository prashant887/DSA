def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def reverse_string(s):
    s = list(s)

    start, end = 0, len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1

    while s[start]==' ':
        start=start+1

   # s=s[start:end+1]
   # print(s)
   # start, end = 0, len(s) - 1


    reverse_word(s, start, end)
    start = end = 0
    while end < len(s):
        if s[end] == ' ':
            reverse_word(s, start, end - 1)
            start = end + 1
        end += 1
    reverse_word(s, start, end - 1)
    return ''.join(s)


s = " the sky is blue "
print("[{}]".format(reverse_string(s)))