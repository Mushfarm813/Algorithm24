def string_matching(T,P):
    n=len(T)
    m=len(P)
    for i in range(n-m+1):
        j=0
        while j<m and P[j]==T[i+j]:
            j=j+1
        if j==m:
            return i
    return -1

text="ALGORITHM IS FUN"
pattern ="S F"
print(pattern,'in',text,'-->',string_matching(text,pattern))
pattern="GR"
print(pattern,'in',text,'-->',string_matching(text,pattern))