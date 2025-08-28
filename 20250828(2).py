1.##N = int(input("정수 입력 : "))
##num = 0
##for i in range (1, N+1) :
##  if N%i == 0 :
##    num += 1
##print(num)

2.##N = int(input("정수 입력 : "))
##num = 0
##for i in range(1, N+1) :
##  num += i
##print(num)

3.##N = input("문자열 입력 : ")
##M = int(input("정수 입력 : "))
##print(N * M)

4.##i = 1
##n = input(" ")
##n = int(n)
##
##while i < n :
##  print(i, i+1)
##  i += 1

5.##a = input("점수 입력 : ")
##b = input("점수 입력 : ")
##c = input("점수 입력 : ")
##
##a = int(a)
##b = int(b)
##c = int(c)
##
##if a + b + c // 3 >= 60 :
##  print("YES")
##else :
##  print("NO")

6.##a = 1
##while a < 100 :
##  if a%3 == 0 or a%7 == 0 :
##    print(a, end = " ")
##  a += 1

7.##n = int(input("정수 입력 : "))
##m = int(input("정수 입력 : "))
##a = n%m
##print(a)

8.##arr  = list(map(int,input("리스트 입력 : ").split()))
##num = 0
##a = [ ]
##for i in arr :
##  if i%5 == 0 :
##    a.append(i)
##    print(i, end = ' ')
##print()
##
##print(len(a),sum(a), round(sum(a) / len(a), 2))

9.##N = input("문자열 입력 : ")
##M = input("문자 입력 : ")
##for ch in N :
##  if ch != M :
##    print(ch, end = "")

n = int(input())
arr = list(map(int, input(). split()))

count = [0] * 10 # [0,0,0,0,0,0,0,0,0,0]
for X in arr :
  count[X] += 1

for c in count :
  print(c)
  

  

  
    

  
