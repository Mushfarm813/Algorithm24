def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div 

a=int(input("최대공약수를 구할 수를 입력하시오: "))
b=int(input("최대공약수를 구할 수를 입력하시오: "))

alist = divisor(a)

gcd_result = None   
for divisor in alist:
    if b % divisor == 0:
        gcd_result = divisor 

print(a, "의 약수 =", alist)
print(a, "과", b, "의 최대공약수 =", gcd_result)
