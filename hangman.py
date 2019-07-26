def hangman(word):
    wrong = 0
    theMan = [
       "___________",
       "|     |    ",
       "|     O    ",
       "|    /|\   ",
       "|   / | \  ",
       "|    / \   ",
       "|  _/   \_ ",
       "|__________"
   ]
    emptyStage = [
        "___________",
       "|          ",
       "|          ",
       "|          ",
       "|          ",
       "|          ",
       "|          ",
       "|__________"
    ]
    letters = list(word)
    board  = ["_"] * len(word)
    win = False
    print("DO YOU TO PLAY A GAME?")
    print(emptyStage)
    print(" ".join(board))
    
    while win == False:
        message = "Guess a letter: "
        guess = input(message)
        

        if guess in letters:
            while guess in letters:
                index = letters.index(guess)
                board[index] = guess
                letters[index] = "#"
            print(" ".join(board))
        else:
            wrong += 1
            #print("Hello")
            print("\n".join(theMan[0: wrong + 2]))
            #print(" ".join(board))

        if "_" not in board:
            win = True
            print("CONGRATS YOU WON!")

        if wrong > 5:
            print("YOU LOSE!".format(word))
            break
hangman("asurion")


