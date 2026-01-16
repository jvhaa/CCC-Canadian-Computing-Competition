for i in range(int(input())):
  num = int(input())
  ans = 0
  for i in range(1, num):
    if num % i == 0:
      ans += i
  if ans > num:
    print(f"{num} is an abundant number.")
  elif ans == num:
    print(f"{num} is a perfect number.")
  else:
    print(f"{num} is a deficient number.")
