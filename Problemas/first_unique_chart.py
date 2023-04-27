def firstUniqChar(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1


firstUniqChar('parcepace')
