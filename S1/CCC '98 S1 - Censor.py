for i in range(int(input())):
    sentence = input().strip().split()
    for word in sentence:
        if len(word) == 4:
            sentence[sentence.index(word)] = "****"
    print(" ".join(sentence))
