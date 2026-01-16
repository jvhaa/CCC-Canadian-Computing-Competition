import math
num, divisor = int(input()), int(input())

ans = num//divisor
remainder = num - ans*divisor

if ans != 0:
    print(ans, end ="")

if ans != 0 and remainder != 0:
    print(" ", end="")

if remainder != 0:
    for i in range(min(remainder, divisor), 0, -1):
        if (remainder/i) == (remainder//i) and (divisor/i) == (divisor//i):
            remainder //= i
            divisor //= i
            break
    print(f"{remainder}/{divisor}",end="")
print()
