import sys
input = sys.stdin.readline
lengthed = int(input())
for i in range(lengthed):
    print("The bit patterns are")
    length, ones = list(map(int, input().split()))

    end = "0"*(length-ones) + "1"*ones
    num = "1"*ones + "0"*(length-ones)
    while True:
      print(num)
      if num == end:
        break
      now = len(num)
      oned = 0
      final_one = 0
      while True:
        future = num.rfind("1", 0, now)
        if future == -1:
          break
        if future == now-1:
          oned += 1
        else:
          final_one = future
          break
        now = future
      num = num[:final_one] + "0" + "1" + "1"*oned + "0" * (len(num)-final_one-2-oned)
    if i != lengthed-1:
        print()
