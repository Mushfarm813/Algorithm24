def factorial_iter(n):
    result=1
    for k in range(1,n+1):
        result=result*k
    return result
n=int(input("정수 n 값을 입력하시오: "))
factorial_iter(n)
print(n, "!의 값은", factorial_iter(n), "입니다.")