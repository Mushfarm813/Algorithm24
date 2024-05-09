def kth_smallest_sort(A, k):
    A.sort() 
    return A[k-1]
A=[7, 10, 4, 3, 20, 15]
A.sort()
A.sort(reverse=True)
B = sorted(A, reverse=True)

print("[정렬기법] 3번째 작은 수: ", kth_smallest_sort(A, 3)) 
print("[정렬기법] 6번째 작은 수: ", kth_smallest_sort(B, 6))