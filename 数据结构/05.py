def bf(s, t, pos):
    i, j = pos, 0
    m, n = len(s), len(t)
    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j ==n:
        return i - j
    else:
        return -1
a=bf('abcabcac','abcac',0)
a