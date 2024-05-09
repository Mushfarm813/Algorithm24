def sequential_search(A,key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1

arr=[7,4,2,1,6,9,8]
key=9
print("Original: ",arr)
sequential_search(arr,key)
print("Selection: ",key)
