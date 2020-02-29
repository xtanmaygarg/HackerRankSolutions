def minion_game(string):
    vowel = ["A", "E", "I", "O", "U"]
    Stuart = 0
    Kevin = 0
    L = len(string)
    for i in range(len(string)):
        if string[i] in vowel:
            Kevin += L
        else:
            Stuart += L
        L -= 1
    if Stuart > Kevin:
        print("Stuart {0}".format(Stuart))
    elif Kevin > Stuart:
        print("Kevin {0}".format(Kevin))
    else:
        print("Draw")


