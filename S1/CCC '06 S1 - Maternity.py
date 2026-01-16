parA = input()
parB = input()

allowedgenes = set()

for i in range(0, 5):
    geneA = parA[i*2:i*2+2]
    geneB = parB[i*2:i*2+2]
    for a in geneA:
        for b in geneB:
            if a.isupper() or b.isupper():
                allowedgenes.add(a.upper())
            else:
                allowedgenes.add(a.lower())
num = int(input())

for i in range(num):
    child = input()
    for gene in child:
        if gene not in allowedgenes:
            print("Not their baby!")
            break
        elif gene in allowedgenes and gene == child[-1]:
            print("Possible baby.")
