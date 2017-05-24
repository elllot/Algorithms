def word_break_duplicate(s, words):    
    if not s or not words: return s
    W = set(words)
    lengths = set(len(w) for w in words)
    return wb_duplicate(0, s, W, {}, lengths)

def wb_duplicate(piv, s, words, cache, lengths):
    if piv in cache: return cache[piv]
    if piv == len(s): return 1
    cnt = 0
    for i in lengths:
        nxt = piv + i
        if nxt <= len(s):
            word = s[piv:nxt]
            if word in words:
                cnt += wb_duplicate(nxt, s, words, cache, lengths)
    cache[piv] = cnt
    return cnt

def word_break(s, words):    
    if not s or not words: return s
    W = collections.Counter(words)
    lengths = set(len(w) for w in W.keys())
    return wb(0, s, W, {}, lengths)

def wb(piv, s, words, cache, lengths):
    if piv in cache: return cache[piv]
    if piv == len(s): return 1
    cnt = 0
    for i in lengths:
        nxt = piv + i
        if nxt <= len(s):
            word = s[piv:piv+i]
            if word in words and words[word] > 0:
                words[word] -= 1
                cnt += wb(nxt, s, words, cache, lengths)
                words[word] += 1
    cache[piv] = cnt
    return cnt




s = "takebathandcome"
words = ["take", "bath", "hand", "bat", "and", "come"]

print(word_break(s, words))