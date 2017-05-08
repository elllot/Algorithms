def patternArray(p):
    arr = [0 for _ in range(len(p))]
    j = 0
    for i in range(1, len(arr)):
        while j > 0 and p[i] != p[j]:
            j = arr[j-1]
        if p[i] == p[j]: arr[i] = j + 1
        j += 1
    return arr

def kmpSearch(st, pat):
    if not st or not pat or len(pat) > len(st): return False
    if len(pat) == 1: return True if pat in st else False
    arr = patternArray(pat)
    p = i = 0
    while i < len(st) and p < len(arr):
        while p > 0 and pat[p] != st[i]:
            p = arr[p-1]
        if pat[p] == st[i]: p += 1
        i += 1
    return p >= len(arr)

print(kmpSearch("aabaxf", "aba"))
