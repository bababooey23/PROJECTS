import random

loops = 1
points = 0
yestypes = ["yes","yrs","tes","ys","yea","yez","es","yews","yres","res","twa","yse","fuhyea","yah","yessir","yeah","yeh","yap","yep","mhm","yup"]
yestypestoo = set(yestypes)

while loops > 0:
    actualword = input("\nEnter a word: ")
    betchoice = input("You only get points by betting, wanna bet? (yes|no) ")
    if betchoice in yestypestoo:
        guessbet = input("It would guess in less tries than ")
    wordlength = len(actualword)
    fullword = []
    i = 0
    schet = 0
    multiplier = 1

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

    if betchoice in yestypestoo:
        if int(guessbet) > schet:
            print("You got it right!")
        else :
            print("It turned out slower.")

    if betchoice in yestypestoo:

        if wordlength == 1:

            if int(guessbet) < 25:
                print("You're pretty hopeful.")
                if int(guessbet) > schet:
                    multiplier = 2

            if int(schet) < 37:
                points = points + 1 * multiplier
                if multiplier > 1:
                    print("Gained 2 points.")
                else :
                    print("Gained 1 point.")
            else:
                points = points + 0
                print("Gained 0 points.")

        if wordlength == 2:

            if int(guessbet) < 1000:
                print("You're pretty hopeful.")
                if int(guessbet) > schet:
                    multiplier = 2

            if int(schet) < 3000:
                points = points + 10 * multiplier
                if multiplier > 1:
                    print("Gained 20 points.")
                else:
                    print("Gained 10 points.")
            else:
                points = points + 5
                print("Gained 5 points.")

        if wordlength == 3:

            if int(guessbet) < 50000:
                print("You're pretty hopeful.")
                if int(guessbet) > schet:
                    multiplier = 2

            if int(schet) < 150000:
                points = points + 100 * multiplier
                if multiplier > 1:
                    print("Gained 200 points.")
                else:
                    print("Gained 100 points.")
            else:
                points = points + 50
                print("Gained 50 points.")

        if wordlength == 4:

            if int(guessbet) < 1000000:
                print("You're pretty hopeful.")
                if int(guessbet) > schet:
                    multiplier = 2

            if int(schet) < 6000000:
                points = points + 1000 * multiplier
                if multiplier > 1:
                    print("Gained 2000 points.")
                else:
                    print("Gained 1000 points.")
            else:
                points = points + 500
                print("Gained 500 points.")

        if wordlength > 4:

            if int(guessbet) < 10000000:
                print("You're pretty hopeful.")
                if int(guessbet) > schet:
                    multiplier = 2

            if int(guessbet) < 400000000:
                points = points + 10000 * multiplier
                if multiplier > 1:
                    print("Gained 2000 points. was it worth it?")
                else:
                    print("Gained 1000 points. was it worth it?")
            else:
                points = points + 5000
                print("Gained 500 points. was it worth it?")

    print("\nYou got ", points, " points.")
    loops = loops - 1
    loopchoice = input("\nWanna go again?(yes|no) ")
    if loopchoice in yestypestoo:
        loops = loops + 1
    else:
        break
