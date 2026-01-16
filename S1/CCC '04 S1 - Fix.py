for i in range(int(input())):
    prefix = [input() for i in range(3)]
    free = False
    for start in range(len(prefix)-1):
        s = prefix[start]
        for end in range(start+1, len(prefix)):
            e = prefix[end]
            if (s in e and (e.find(s) == 0 or e.find(s) + len(s) == len(e))) or (e in s and (s.find(e) == 0 or s.find(e) + len(e) == len(s))):
                free = True
    print("No" if free else "Yes")
