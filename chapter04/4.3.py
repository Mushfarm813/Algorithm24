def insertion_sort(A):
    n=len(A)
    for i in range(1,n):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key

data=[5,2,6,1,9,7,4]
print("원래의 배열 : ",data)
insertion_sort(data)
print("삽입 정렬 후의 배열 : ",data)