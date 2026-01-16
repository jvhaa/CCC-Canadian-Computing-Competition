def Nasty_number(number):
    divisors = []
    visited = []
    for i in range(1, int(number**0.5)+1):
        l = number // i
        if number % i == 0 and l not in visited:
            visited.extend([i, l])
            divisors.extend([abs(i-l), l+i])
    if len(divisors) != len(set(divisors)):
        return True
    return False

for _ in range(int(input())):
    number = int(input())
    if Nasty_number(number):
        print(f"{number} is nasty")
    else:
        print(f"{number} is not nasty")
