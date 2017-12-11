def lcs(word1, word2):
    row = [0 for _ in range(len(word1) + 1)]
    for r in range(1, len(word2)+1):
        prev = 0
        for c in range(1, len(row)):
            val = prev + 1
            if word2[r-1] != word1[c-1]:
                val = max(row[c-1], row[c])
            row[c], prev = val, row[c] 
    return row[-1]

if __name__ == '__main__':
    one = 'aggtab'
    two = 'gxtxayb'
    print(lcs(one, two))

    three = 'abcdgh'
    four = 'aedfhr'
    print(lcs(three, four))