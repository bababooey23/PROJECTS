import random

actualword = input("Enter a word: ")
wordlength = len(actualword)
fullword = []
i = 0
schet = 0

while True:

    while i < int(wordlength):
        guesspower = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        fullword.append(random.choice(guesspower))
        i = i + 1
    results = "".join(fullword)
    schet = schet + 1
    if results == actualword:
        break
    else :
        print(results, " try number ", schet)
        fullword = []
        i = 0

print("FINALLY! ",results," was guessed with amount of tries: ",schet)