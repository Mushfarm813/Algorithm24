def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div 

num1=int(input("최대공약수를 구할 수를 입력하시오: "))
num2=int(input("최대공약수를 구할 수를 입력하시오: "))

alist = divisor(num1)
blist = divisor(num2)

c_div = []
for divisor in alist:
    if divisor in blist:
        c_div.append(divisor)

if c_div:
    c_div_max = max(c_div)
    print(num1, "의 약수 =", alist)
    print(num2, "의 약수 =", blist)
    print(num1, "과", num2, "의 최대공약수 =",  c_div_max)
