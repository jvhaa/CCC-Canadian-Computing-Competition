for i in range(int(input())):
    subj = int(input())
    verb = int(input())
    obj = int(input()) 
    subjs = [input().strip() for i in range(subj)]
    verbs  = [input().strip() for i in range(verb)]
    objs = [input().strip() for i in range(obj)]
    for sub in subjs:
        for ver in verbs:
            for ob in objs:
                print(f"{sub} {ver} {ob}.")
