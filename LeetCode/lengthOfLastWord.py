def lengthOfLastWord( s: str) -> int:
    length = 1
    n = len(s) - 1
    while n >= 0:
        if s[n] != ' ' and s[n - 1] != ' ':
            length = length + 1
        elif s[n] != ' ' and s[n - 1] == ' ':
            return length
        n = n - 1
    return length

"""
The first while loop moves the pointer i backwards through the string until the first non-whitespace character is found. Then we're ready to start counting the length of the word we just hit, so the second loop increments length and moves i backwards until a whitespace character is found.

Once that whitespace character is found, that means we've finished traversing the word, so the only thing left to do is to return length.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
"""