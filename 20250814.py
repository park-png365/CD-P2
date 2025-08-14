1.##n = int(input("정수입력 : "))
##m = int(input("정수입력 : "))
##for i in range (n ,m+1 ,5) :
##  print(i)

2.##n = int(input())
##nums = list(map(int, input().split()))
##check = False
##for i in range(n) :
##  if (check): print(nums[i], end = ' ')
##  if (nums[i]==10):check = True

##n = int(input())
##nums = list(map(int, input().split()))
##index = -1
##for i in range (n) :
##  if (nums[i] == 10) : index = i
##print(nums[i+1 : ])

3.##n = int(input("정수입력 : "))
##for i in range(n) :
##  spaces = '^' * (n - i - 1)
##  stars = '*' * (2 * i +1)
##  print(spaces + stars + spaces)

4.##n = int(input("정수입력 : "))
##m = int(input("정수입력 : "))
##if n<m :
##  print(n)
##else :
##  print(m)

5.##---중요---
##n = int(input())
##arr = list(map(int, input().split()))
##for i in range(0, n, 2) :
##  print("%d" % [i], end =  " ")

6.##s = input()
##ans = 0
##for i in range(len(s)) :
##  if s[i].isalpha() :
##    ans += 1
##print(ans)

7.##s = input("문자열 입력 : ")
##n = int(input("정수 입력 : "))
##print(s + "+" + str(n))

8.##n = int(input("정수입력 : "))
##m = int(input("정수입력 : "))
##print(max(n, m))

9.##s = input("문자열 입력 : ")
##for i in range(len(s) -2) :
##  print(s[i : i+3], end = ' ' )

10.##s = input("문자열 입력 : ")
##print('\\' + s + '\\')

1.##N = int(input())
##value = N
##add  = 3
##
##while value <= 100 :
##  print(value)
##  value += add
##  add += 3

3.##n = list(input("문자열 입력 : "))
##under_count = 0
##for ch in n :
##  if 'A' < ch <'Z' :
##    under_count += 1
##print(under_count) 

  
