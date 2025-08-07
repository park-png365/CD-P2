6.##a = input("정수 : ")
##for ch in a :
##    if 'a' <= ch <= 'z' or 'A' <= ch <='Z' :
##        print(ch)

7.##a = input("정수 : ")
##for ch in a :
##    if '1' <= ch <= '9' :
##        print(ch)

8.##a = input("정수 : ")
##print(a.swapcase())

9.##a = input("정수 : ")
##a = a[::-1]
##for ch in a :
##    print(ch)

a = input("정수 : ")
upper_count = 0
lower_count = 0
digit_count = 0
etc_count = 0
for ch in a :
    if 'A' <= ch <= 'Z' :
        upper_count += 1
    elif 'a' <= ch <= 'z' :
        lower_count += 1
    elif '1' <= ch <= '9' :
        digit_count += 1
    else :
        etc_count += 1
print("대문자 개수 : " ,upper_count)
print("소문자 개수 : " ,lower_count)
print("숫자 개수 : " ,digit_count)
print("기타문자 개수 : " ,etc_count)

    



