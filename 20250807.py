1.##nums = list(map(int,input().split()))
##print(sum(nums))

2.##data = list(map(int,input().split()))
##print(max(data))

3.##nums = list(map(int,input().split()))
##for n in nums :
##  if n % 2 ==0 :
##    print(n)

4.##nums = list(map(int,input().split()))
##cnt = 0
##for n in nu ms :
##  if 5 <= n :
##    cnt += 1
##print(cnt)

5.##nums = list(map(int,input().split()))
##reversed_nums = nums[::-1]
##print(*reversed_nums)

6.##nums = list(map(int,input().split()))
##for n in nums :
##  if n%2 == 1 :
##    print(n)

7.##nums = [10,15,8,20]
##for i in range(len(nums)-1) :
##  print(abs(nums[i] - nums[i+1]))

8.##number = 0
##nums = list(map(int,input().split()))
##count = sum(nums)
##num = len(nums)
##number = count / num
##for n in nums :
##  if n > number :
##    print(n)

9.##nums = list(map(int,input().split()))
##max = max(nums)
##min = min(nums)
##print(max)
##print(min)

10.##nums = list(map(int,input().split()))
##arr = []
##for n in nums :
##  if n%2 == 0 :
##    arr.append(n)
##
##print(arr[::-1])

1.##nums = list(map(int,input().split()))
##max_len = 1
##cur_len = 1
##for i in range(1,len(nums)) :
##  if nums[i] - nums[i-1] > 0 :
##    cur_len += 1
##    max_len = max(max_len, cur_len)
##  else :
##    cur_len = 1
##print(max_len);
  
2.##nums = list(map(int,input().split()))
##max_val = max(nums)
##min_val = min(nums)
##print(max_val - min_val)

3.##nums = list(map(int,input().split()))
##max_diff = 0
##for i in range(len(nums)-1) :
##  diff = abs(nums[i] - nums[i+1])
##  print(diff)
##  if diff  > max_diff :
##    max_diff  = diff
##print(max_diff)

4.##nums = list(map(int,input().split()))
##print(nums.count(nums[-1]))

5.##nums = list(map(int,input().split()))
##num = 0
##for n in nums :
##  if 5 <= n :
##    num += n
##print(num)

6.##nums = list(map(int,input().split()))
##count = 0
##for n in nums :
##  if n%2 == 0 :
##    print (n)
##    count += 1
##print(count)

7.##nums = list(map(int,input().split()))
##for n in nums :
##  n = n*2
##  print(n, end=" ")


8.##number = 0
##nums = list(map(int,input().split()))
##count = sum(nums)
##num = len(nums)
##number = count / num
##for n in nums :
##  if n > number :
##    print(n)


9.##nums = list(map(int,input().split()))
##for n in nums :
##  if n > nums[0] :
##    print(n)

10.##nums = list(map(int,input().split()))
##print(nums[::-1])




