def checker(index, s, offset):
    ans, i, j = 1+offset*2, index-1-offset, index+1+offset
    while i >= 0 and j < len(s) and s[i] == s[j]:
        ans += 2
        i -= 1; j += 1
    return ans

def process(s):
    temp = len(s)*2+1
    arr = [0 for _ in range(temp)]
    cArray, dBit = [], True
    for i in range(temp):
        if dBit: cArray.append('$')
        else: cArray.append(s[i//2])
        dBit = not dBit
    s = ''.join(cArray)
    return arr, s

def LPSeven(arr, s):
    return

def LPSodd(arr, s):
    piv = 0
    while piv < len(s):
        arr[piv] = checker(piv, s, arr[piv]//2)
        step = arr[piv]//2
        lBound, hBound = max(0,piv - step), piv + step
        if hBound >= len(s)-1: break
        j = piv-1
        while piv <= hBound:
            piv += 1
            arr[piv] = arr[j] if j - arr[j]//2 >= lBound else 1 + (j-lBound) * 2 # low bound check
            if arr[j] + piv >= hBound and j - arr[j]//2 >= lBound: break
            j -= 1
    I = mx = 0
    for i,v in enumerate(arr):
        if v > mx: mx = v; I = i 
    step = mx//2
    return I, s[I-step:I+step+1]

# Manacher's Algorithm
def LPS(s):
    if not s: return ""
    arr = []
    """
    if len(s) % 2 == 0: 
        arr, s = process(s)
        return LPSeven(arr, s)
    else: 
    """
    arr = [0 for _ in range(len(s))]
    return LPSodd(arr, s)
        
    """
    piv = 0
    while piv < len(s):
        arr[piv] = checker(piv, s)
        if arr[piv] <= 3: piv += 1
        else:
    """

def Manacher(s):
    T = '#'.join('^{}$'.format(s))#[1:-1]
    P = [0] * len(T)
    center = right = 0
    for i in range(1, len(T)-1):
        P[i] = (right > i) and min(right - i, P[2 * center - i]) 
        # checking longest palindrome at current index
        while T[i - P[i] - 1] == T[i + P[i] + 1]:
            P[i] += 1
        if i + P[i] >= len(T)-2: break
        # if palindrome length expands beyond right bound, reset center
        if i + P[i] > right:
            center, right = i, i + P[i]
    V, I = max((v, i) for i, v in enumerate(P))
    return s[(I - V)//2: (I + V)//2]

#print(LPS("abaxabaxabb"))
print(Manacher("abaxabaxabb"))
