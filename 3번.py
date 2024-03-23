def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div   #입력된 수의 약수를 찾아 리스트에 저장하는 함수

num1 = 60
num2 = 28

alist = divisor(num1)

gcd_result = None   
for divisor in alist:
    if num2 % divisor == 0:
        gcd_result = divisor  #alist의 값으로 28을 나누며 최대공약수를 찾는다.

print(num1, "의 약수 =", alist)
print(num1, "과", num2, "의 최대공약수 =", gcd_result)
