x = [[17,72],
    [14,65],
    [43,23]]
trans = [[0, 0, 0],
    [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        trans[j][i] = x[i][j]
for k in trans:
    print(k)