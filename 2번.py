def divisor(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    return div  ##입력된 수의 약수를 찾아 리스트에 저장하는 함수

num1 = 60
num2 = 28

alist = divisor(num1)
blist = divisor(num2)  #각 리스트에 약수를 저장

c_div = []
for divisor in alist:
    if divisor in blist:
        c_div.append(divisor)  #alist의 수가 blist에도 존재하면 이를 c_div리스트에 추가

if c_div:
    c_div_max = max(c_div)
    print(num1, "의 약수 =", alist)
    print(num2, "의 약수 =", blist)
    print(num1, "과", num2, "의 최대공약수 =",  c_div_max)
