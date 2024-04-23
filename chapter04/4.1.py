# 알고리즘 코드
def factorial_recur(n):
    if n==1:
        return 1
    else:
        return (n*factorial_recur(n-1))
    
n=int(input("정수 n 값을 입력하시오: "))
result = factorial_recur(n)
print(n, "!의 값은", result, "입니다.")