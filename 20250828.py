8.##N = int(input("정수 입력 : "))
##for i in range(0,N) :
##  print("a" * (N-i) + "z" * i, end = ""

9.##arr = list(map(int, input("리스트 입력 : ").split()))
##arr[2:7] = arr[2 : 7][::-1]
##print(arr)

A = int(input("정수 입력 : "))
B = int(input("정수 입력 : "))
C = int(input("정수 입력 : "))
if A == B and A == C :
  print(A)
elif A == B:
  print(C)
elif B == C:
  print(A)
elif A == C:
  print(B)
elif A != B and B!= C :
  print(max(A, B, C))

