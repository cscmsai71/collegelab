X = [[10,11,12],
    [13,14,15],
    [16 ,17,18]]

Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]

result = [[X[i][j] - Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)