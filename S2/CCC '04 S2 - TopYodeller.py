yodellers, rounds = list(map(int, input().split()))

yodeller = [[0, i+1, 0] for i in range(yodellers)]

for i in range(rounds):
    points = list(map(int, input().split()))
    for i in range(len(points)):
        yodeller[i][0] += points[i]
    pointer = sorted(yodeller, key = lambda x:x[0], reverse=True)
    rank_lag = 0
    for yo in range(len(pointer)):
        rank = yo+1
        if yo+1 > 1:
          if yodeller[pointer[yo][1]-1][0] == yodeller[pointer[yo-1][1]-1][0]:
            rank_lag += 1
            rank -= rank_lag
        yodeller[pointer[yo][1]-1][2] = max(yodeller[pointer[yo][1]-1][2], rank)

yodeller = sorted(yodeller, key = lambda x: (x[0], 0-x[1]), reverse=True)
max = yodeller[0][0]

for i in range(len(yodeller)):
  if yodeller[i][0] == max:
    print(f"Yodeller {yodeller[i][1]} is the TopYodeller: score {yodeller[i][0]}, worst rank {yodeller[i][2]}")
  else:
    break
