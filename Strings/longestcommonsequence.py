def LCS(s1, s2):
    l1, l2 = len(s1)+1, len(s2)+1
    row = [0] * l1
    for i in range(1, l2):
        prev = 0
        for j in range(1, l1):
            prev, row[j] = row[j], prev+1 if s1[j-1] == s2[i-1] else max(row[j-1], row[j])
    return row[-1]

print(LCS("abcdafa", "acbdfae"))
