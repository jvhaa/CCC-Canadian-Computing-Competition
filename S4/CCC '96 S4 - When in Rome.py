import sys
input = sys.stdin.readline

roman_numberals = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

reverse = {
  "M":1000,
  "CM":900,
  "D":500,
  "CD":400,
  "C":100,
  "XC":90,
  "L":50,
  "XL":40,
  "X":10,
  "IX":9,
  "V":5,
  "IV":4,
  "I":1
}

for test_cases in range(int(input())):
  e = input().strip()
  equation = e[:-1].split("+")
  added = []
  for i in equation:
    order = []
    for character in i:
      order.append(roman_numberals[character])
    addition = []
    for od in range(len(order)-1):
      if order[od] < order[od + 1]:
        addition.append(-order[od])
      else:
        addition.append(order[od])
    addition.append(order[-1])
    added.append(sum(addition))
  ans = sum(added)
  if ans < 1001:
    roman = ""
    while ans > 0:
      for key, value in reverse.items():
        if ans >= value:
          ans -= value
          roman += key
          break
    print(f"{e}{roman}")
  else:
    print(f"{e}CONCORDIA CUM VERITATE")
