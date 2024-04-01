def find_max(A):
    max = A[0]  
    for i in A:
        if i > max:
            max = i
    return max

A = [3, 7, 2, 9, 4, 1, 6, 8, 5]

max_value = find_max(A)
print("최댓값:", max_value)