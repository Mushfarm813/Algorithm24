def knapSack_dc(W,wt,val,n):
    if n==0 or W==0:
        return 0
    
    if (wt[n-1]>W):
        return knapSack_dc(W,wt,val,n-1)
    else:
        valWithout=knapSack_dc(W,wt,val,n-1)
        valWith=val[n-1]+knapSack_dc(W-wt[n-1],wt,val,n-1)
        return max(valWith,valWithout)

val=[30,50,130,200,100,80]
wt=[1,5,6,2,3,5]
W=16
n=len(val)
print("0-1배낭문제(분할 정복): ",knapSack_dc(W,wt,val,n))