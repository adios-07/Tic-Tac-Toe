import random

def PrintGameState(GS):
    PgS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(9):
        if(GS[i] == 1): PgS[i] = 'X'
        elif(GS[i] == 5): PgS[i] = 'O'
    print("_________________________________________________")
    print( " _______________________")
    print( "|       |       |       |")
    print(f"|   {PgS[0]}   |   {PgS[1]}   |   {PgS[2]}   |")
    print( "|       |       |       |")
    print( "|-------|-------|-------|")
    print( "|       |       |       |")
    print(f"|   {PgS[3]}   |   {PgS[4]}   |   {PgS[5]}   |")
    print( "|       |       |       |")
    print( "|-------|-------|-------|")
    print( "|       |       |       |")
    print(f"|   {PgS[6]}   |   {PgS[7]}   |   {PgS[8]}   |")
    print( "|       |       |       |")
    print( " ----------------------- ")

def BotPick(GS, X):
    che = random.randint(1,9)
    while(GS[che-1] != 0): che = random.randint(1,9)
    if(X): GS[che-1] = 1
    else: GS[che-1] = 5


def MyPick(GS, X):
    che = int(input("Pick an Empty Slot: "))
    if(che >= 1 and che <= 9 and GS[che-1] == 0):
        if(X): GS[che-1] = 5
        else: GS[che-1] = 1
    else:
        print("Wrong choice, Picking random since ure so dumb :P")
        BotPick(GS, not X)

def HasEnded(GS):
    Filled = 2
    for i in range(len(GS)):
        if(GS[i] == 0): Filled = 0
    
    winCond = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in winCond:
        sum = 0
        for j in i:
            sum+=GS[j-1]
        if(sum == 15): 
            return 5
        elif(sum == 3): 
            return 1
    return Filled
            

def main():
    GameState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    GameEnded = 0
    Turn = 1

    print("Lets Play a Game!")
    ch = int(input("Choose 1 for X and 2 for O: "))
    X = 0
    match ch:
        case 1:
            X = 0
        case 2:
            X = 1
        case _:
            print("Wrong Choice picked!, Giving Default pick: 1")
            exit()

    print("Lets Start Shall we!")
    if(X == 0): print("You chose X")
    else: print("You chose O")
    while(GameEnded == 0):
        PrintGameState(GameState)
        if((Turn+X)%2 == 0): 
            print("Bot's Turn")
            Turn += 1
            BotPick(GameState, X)
        else:
            print("Your Turn")
            Turn += 1
            MyPick(GameState, X)
        GameEnded = HasEnded(GameState)

    PrintGameState(GameState)
    print("------GAME OVER------")
    if(GameEnded == 2): print("The Game was a DRAW!")
    elif(GameEnded == 5): print("O won")
    elif(GameEnded == 1): print("X won")
    print("Hope You Enjoyed :)")


if(__name__ == "__main__"):
    main()
