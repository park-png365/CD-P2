1.##N = input("문자 입력 : ")
##print(N.lower())

2.##N = int(input("정수 입력 : "))
##for i in range(0, N) :
##  blank = N - i
##  star = 2 * i + 1
##  print(" " * blank  + "*" * star + " " * blank)

3.##print("Python:\\test")

4.##a, b = map(int,input("").split())
##
##if a<b :
##  print(a,"-",b,"=",a-b)
##elif a>b :
##  print(a, "+" ,b, "=",a + b)
##else :
##  print(a, "=" ,b)

hap = 0
i = 1

n = int(input(""))
while i  <= n :
  if i%3 == 0 :
    hap += i
  i += 1

print(hap)
