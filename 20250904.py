1.##n = input("문자 입력 : ")
##print(n.lower())

2.##n = int(input("숫자 입력 : "))
##blank = 0
##star = 0
##for i in range(0, n) :
##    
##    blank =  n - i
##    star = 2 * i + 1
##    print(blank * " " + star * "*" + blank * " ")

3.##print("Python:\\test")

4.##a, b = map(int,input("").split())
##
##if a<b :
##  print(a, "+" ,b, "=",a + b)
##elif a>b :
##  print(a,"-",b,"=",a-b)
##else :
##  print(a, "=" ,b)

7.##n = int(input("숫자 입력 : "))
##minute = 0
##second = 0
##minute = n % 60
##second = n // 60
##print(second, minute)

a, b = map(int,input("").split())
for i in range (0, a) :
    for j in range (0, b) :
        print(j * "*")

