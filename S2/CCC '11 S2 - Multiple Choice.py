num = int(input())

answers = [input() for i in range(num)]
answered = [input() for i in range(num)]
correct = 0

for x, y in zip(answers, answered):
    if x == y:
        correct += 1
        
print(correct)
