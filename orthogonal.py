def orthogonal(Q,m,n):
    if m != n:
        return False
    else:
        for i in range(0,n):
            for j in range(0,n):
                sum=0
                for k in range(0,n):
                    sum=sum +round(Q[i] [k] * Q[i] [k])
                    if i!=j and sum!=0:
                        return False
                        if i==j and sum!=1:
                            return False
                        else:
                            return True
Q=[[0.68567,0.12975,-0.71626],
[0.14807,0.93855,0.31176],
[0.71269,-0.31982,0.62433]]
if orthogonal(Q,3,3):
    print("the matrix is orthogonal")
else:
    print("the matrix is not orthogonal")

