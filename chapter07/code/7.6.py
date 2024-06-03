def knapSack_dp(W,wt,val,n):
    A=[[0 for x in range(W+1)]for x in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1]>w:
                A[i][w]=A[i-1][w]
            else:
                valWith=val[i-1]+A[i-1][w-wt[i-1]]
                valWithout=A[i-1][w]
                A[i][w]=max(valWith,valWithout)

    return A[n][w]

val=[30,50,130,200,100,80]
wt=[1,5,6,2,3,5]
W=16
n=len(val)
print("0-1배낭문제(동적 계획): ",knapSack_dp(W,wt,val,n))