def hash(st, base):
    if not st: return 0
    res, exp = 0, 1
    for i,v in enumerate(st):
        res += exp * ord(v)
        exp *= base 
    return res

def rehash(st, prev, start, pLength, base):
    if start+pLength >= len(st): return -1
    if start == 0: return hash(st[:pLength+1], base)
    return (prev - ord(st[start-1])) / base + (base ** pLength) * ord(st[start+pLength])

def strcomp(st, pt, start):
    if start + len(pt)-1 >= len(st): return False
    for i in range(len(pt)):
        if st[start+i] != pt[i]: return False
    return True

def rabinKarp(st, pt):
    if not st or not pt or len(pt) > len(st): return False
    base = 101 # any prime number
    pHash, sHash = hash(pt, base), 0
    for i in range(len(st)-len(pt)+1):
        sHash = rehash(st, sHash, i, len(pt)-1, base)
        if sHash == pHash and strcomp(st, pt, i): return True, i
    return False, -1

def rabinKarpMulti(st, arr):
    if not st or not arr: return False
    base = 101 # any prime number
    hArr = [hash(s, base) for s in arr]
    mn, sHash = len(min(arr, key=lambda x: len(x))), [0] * len(arr)
    for i in range(len(st)-mn+1):
        sHash = [rehash(st, sHash[a], i, len(v)-1, base) for a,v in enumerate(arr)]
        for h,v in enumerate(hArr):
            if v == sHash[h] and strcomp(st, arr[h], i): return True, i, arr[h]
    return False, -1, ""

strng = "cantfightitremix"
comp = "fight"
cArray = ["fightr", "it"]
print(rabinKarpMulti(strng, cArray))
