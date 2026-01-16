tests, length = map(int, input().split())

heavy = {}
order = {"heavy" : "light",
	"light" : "heavy"}

for i in range(tests):
	word = input().strip()
	for letter in "qwertyuiopasdfghjklzxcvbnm":
		if word.count(letter) > 1:
			heavy[letter] = "heavy"
		else:
			heavy[letter] = "light"
	weight = heavy[word[0]]
	for i in range(1, length):
		if heavy[word[i]] != order[weight]:
			print("F")
			break
		weight = order[weight]
	else:
		print("T")
