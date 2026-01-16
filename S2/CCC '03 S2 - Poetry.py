import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(int(input())):
    last = []
    rhyme = []
    for poems in range(4):
        poem = input().split()
        last.append(poem[-1].lower()) 
    for word in last:
        min_index = float('inf')
        for vowel in vowels:
            if vowel in word:
              min_index = min(word[::-1].find(vowel), min_index)
        if min_index != float('inf'):
          rhyme.append(word[len(word)-min_index-1:])
        else:
          rhyme.append(word)
    if rhyme[0] == rhyme[1] == rhyme[2] == rhyme[3]:
        print("perfect")
    elif rhyme[0] == rhyme[1] and rhyme[2] == rhyme[3]:
        print("even")
    elif rhyme[0] == rhyme[2] and rhyme[1] == rhyme[3]:
        print("cross")
    elif rhyme[0] == rhyme[3] and rhyme[2] == rhyme[1]:
        print("shell")
    else:
        print("free")
