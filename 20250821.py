1.##N = int(input("정수 입력 : "))
##M = 0
##while N<100 :
##  print(N)
##  M = M+3
##  N = N+M

2.##N = int(input("정수 입력 : "))
##for i in range(N) :
##  print(i * "-" + (2*(N-i)-1) * "*" + i* "-")

3.##N = input("문자열 입력 : ")
##upper_count = 0
##for ch in N :
##  if "A" <= ch <= "Z":
##    upper_count += 1
##print(upper_count)

4.##N = int(input("리스트 입력 : "))
##arr = list(map(int, input().split()))
##ans = 0
##for a in arr :
##  if a == 3 or a == 6 or a == 9 :
##    ans += 1
##print("%d"%ans)

5.##s1 = input("문자열 입력 : ")
##s2 = input("문자열 입력 : ")
##s3 = input("문자열 입력 : ")
##print(s3, s2, s1, sep = "\n")

6.##s1 = input("문자열 입력 : ")
##s2 = input("문자열 입력 : ")
##print("Yes" if  s1 == s2 else "No")

7.##s = input()
##for i in range(len(s)) :
##  for j in range(i + 1) :
##    print(s[j], end = ' ')
##  print()

9.##s = input()
##for i in range(len(s)) :
##  print(s[i], end = " ")
##  if  i != len(s) -1 :
##    print("/", end = " ")

10.##n  = int(input())
##arr = list(map(int,input().split()))
##for i in range(n) : 
##  cnt = 0
##  for j in range(1, arr[i]+1) :  
##    if arr[i] % j == 0:
##      cnt += 1
##  if cnt == 2 :
##    print(arr[i])
    


