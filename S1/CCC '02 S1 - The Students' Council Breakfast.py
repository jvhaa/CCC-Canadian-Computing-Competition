import sys

prices = {
    "PINK": 0,
    "GREEN": 0,
    "RED": 0,
    "ORANGE": 0,
}

for colour in prices:
    prices[colour] = int(sys.stdin.readlines(1)[0])

raised = int(sys.stdin.readlines(1)[0])
combination = 0
minimum = float('inf')

for i in range(raised // prices["PINK"] + 1):
    for l in range(raised // prices["GREEN"] + 1):
        for j in range(raised // prices["RED"] + 1):
            for k in range(raised // prices["ORANGE"] + 1):
                if (i * prices["PINK"]) + (l * prices["GREEN"]) + (j * prices["RED"]) + (k * prices["ORANGE"]) == raised:
                    print("# of PINK is", i, "# of GREEN is", l, "# of RED is", j, "# of ORANGE is", k, sep=" ")
                    combination += 1
                    minimum = min(i + l + j + k, minimum)

print(f"Total combinations is {combination}.")
print(f"Minimum number of tickets to print is {minimum}.")
