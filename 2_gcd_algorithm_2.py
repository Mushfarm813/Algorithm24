def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div 

num1=int(input("최대공약수를 구할 수를 입력하시오: "))
num2=int(input("최대공약수를 구할 수를 입력하시오: "))

alist = divisor(num1)

gcd_result = None   
for divisor in alist:
    if num2 % divisor == 0:
        gcd_result = divisor 

print(num1, "의 약수 =", alist)
print(num1, "과", num2, "의 최대공약수 =", gcd_result)
