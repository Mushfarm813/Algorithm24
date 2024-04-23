# 4.10코드
def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

# 4.11코드
def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    
    if (pos+ 1 == left+k):
        return A[pos]
    elif(pos+1 > left+k):
        return quick_select(A, left, pos-1, k)
    else :
        return quick_select(A, pos+1, right, k-(pos+1-left))

# 4.12코드
def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high) : # 왼쪽의 작은수가 오른쪽의 큰수보다 작으면 계속 실행
        while low <= right and A[low] <= pivot : low += 1
        while high >= left and A[high]> pivot : high-= 1
        
        if low < high :  # 왼쪽과 오른쪽이 만나서 교차하게되면 서로 교환을 해준다
            A[low], A[high] = A[high], A[low]
            
    A[left], A[high] = A[high], A[left]  # 처음에 고정된 피벗을 high 위치와 교환한다
    return high                          # 피벗의 위치로 반환

#실행코드(main)
array = [10, 30, 25, 17, 46, 9, 216, 223, 1]
print("입력 리스트= ",array)
print("[정렬기법] 2번째 작은 수:", kth_smallest_sort(array, 2))
print("[정렬기법] 5번째 작은 수:", kth_smallest_sort(array, 5))
n = len(array)
print("[축소기법] 4번째 작은 수:", quick_select(array, 0, n-1, 4))
print("[축소기법] 8번째 작은 수:", quick_select(array, 0, n-1, 8))