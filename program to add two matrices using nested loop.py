x = [[2, 4, 3],
    [4, 5, 6],
    [7, 8, 9]]

y = [[3, 4, 1],
    [2, 7, 8],
    [4, 3, 5]]

add = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x)):
        add[i][j] = x[i][j] + y[i][j]

for k in add:
    print(k)
