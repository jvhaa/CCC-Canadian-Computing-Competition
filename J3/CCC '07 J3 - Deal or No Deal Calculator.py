cases = {
    1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000, 6: 25000, 7: 50000, 8: 100000, 9: 500000, 10: 1000000
}
for value in [int(input()) for _ in range(int(input()))]:
    cases.pop(value, None)
print("deal" if int(input()) >= sum(cases.values()) / len(cases) else "no deal")
