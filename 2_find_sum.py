def find_sum(A):
     sum=0
     for i in A:
          sum+=i
     return sum

A=[3,45,543,234,123]

a=find_sum(A)
print("리스트의 합: ",a)