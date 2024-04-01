def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div 

a=int(input("최대공약수를 구할 수를 입력하시오: "))
b=int(input("최대공약수를 구할 수를 입력하시오: "))

alist = divisor(a)
blist = divisor(b)

c_div = []
for divisor in alist:
    if divisor in blist:
        c_div.append(divisor)

if c_div:
    c_div_max = max(c_div)
    print(a, "의 약수 =", alist)
    print(b, "의 약수 =", blist)
    print(a, "과", b, "의 최대공약수 =",  c_div_max)

