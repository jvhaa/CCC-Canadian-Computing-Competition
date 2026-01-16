import sys

n = -1

while (n!=0):
    n = int(sys.stdin.readlines(1)[0])
    if (n > 0):
        width = int(n ** 0.5)
        while n % width != 0:
            width -= 1
        
        height = n // width
        
        print("Minimum perimeter is", ((width+height)*2), "with dimensions", width, "x",  height, sep = " ")
