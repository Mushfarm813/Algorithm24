def n_square(n):
    square=n*n
    return square

n=int(input("제곱할 정수 n의 값을 입력하시오: "))
result=n_square(n)
print(n,"제곱의 값은",result,"입니다.")