def perfect(start, end):
    answer = []
    for i in range(start, end+1):
        divisors = sum(l for l in range(1, i) if i % l == 0)
        if i == divisors:
            answer.append(divisors)
    return answer
    
def cubed(start, end):
    answer = []
    for i in range(start, end+1):
        cubes = sum([int(l)**3 for l in str(i)])
        if cubes == i:
            answer.append(cubes)
    return answer

p = perfect(1000, 9999)
c = cubed(100, 999)

print(" ".join(map(str, p)))
print(" ".join(map(str, c)))
