import sys
input = sys.stdin.readline
matrixs = int(input())

matrices = []

for i in range(matrixs):
  r, c = map(int, input().split())
  matrix = []
  for row in range(r):
    matrix.append(list(map(int, input().split())))
  matrices.append(matrix)

def Quantum_op(matrixa, matrixb):
  result = []
  for arraya in matrixa:
    for arrayb in matrixb:
      subresult = []
      for numa in arraya:
        for numb in arrayb:
          subresult.append(numa * numb)
      result.append(subresult)
  return result

while len(matrices) > 1:
  matrices.append(Quantum_op(matrices.pop(0), matrices.pop(0)))

max_num = -float('inf')
min_num = float('inf')
max_row = -float('inf')
min_row = float('inf')
max_col = -float('inf')
min_col = float('inf')

matrices = matrices[0]

for i in range(len(matrices[0])):
  total = 0
  for k in range(len(matrices)):
    total += matrices[k][i]
  max_col = max(max_col, total)
  min_col = min(min_col, total)

for i in range(len(matrices)):
  d = matrices[i]
  max_num = max(max_num, max(matrices[i]))
  min_num = min(min_num, min(matrices[i]))
  max_row = max(max_row, sum(matrices[i]))
  min_row = min(min_row, sum(matrices[i]))

print(max_num)
print(min_num)
print(max_row)
print(min_row)
print(max_col)
print(min_col)
