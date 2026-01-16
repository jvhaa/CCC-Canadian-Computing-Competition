def crystalSquaresatX(m,x):
    if m >= 1:
        power = 5 ** (m-1)
        location = x // power
        if location == 0 or location == 4:
            return 0
        elif location == 1 or location == 3:
            return 1 * power + crystalSquaresatX(m - 1, x % power)
        elif location == 2:
            return 2 * power + crystalSquaresatX(m - 1, x % power)
    
    return 0


# file input
T = int(input())
for t in range(T):
    m, x, y = list(map(int, input().split()))
    if y < crystalSquaresatX(m,x):
        print ("crystal")
    else:
        print ("empty")
