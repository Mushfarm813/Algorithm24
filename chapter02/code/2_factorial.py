def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("n!에 들어갈 정수 n값을 입력하시오: "))

result = factorial(n)
print(n, "!의 값은", result, "입니다.")
