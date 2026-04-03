import random

loops = 1

while loops > 0:
    actualword = input("\nEnter a word: ")
    betchoice = input("Wanna bet?(yes|no) ")
    if betchoice == "yes":
        guessbet = input("It would guess in less tries than ")
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
    if betchoice == "yes":
        if int(guessbet) > schet:
            print("You got it right!")
        else :
            print("It turned out slower.")
    if betchoice == "yes":
        if wordlength == 1:
            if int(guessbet) < 25:
                print("You're pretty hopeful.")
        if wordlength == 2:
            if int(guessbet) < 1000:
                print("You're pretty hopeful.")
        if wordlength == 3:
            if int(guessbet) < 50000:
                print("You're pretty hopeful.")
        if wordlength == 4:
            if int(guessbet) < 1000000:
                print("You're pretty hopeful.")
        if wordlength > 4:
            if int(guessbet) < 10000000:
                print("You're pretty hopeful.")
    loops = loops - 1
    loopchoice = input("Wanna go again?(yes|no) ")
    if loopchoice == "yes":
        loops = loops + 1
    else:
        break
