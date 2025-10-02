import random
import Smart_Bot as SB

def PrintGameState(GS, Ply, Bot):
    PgS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(9):
        if(GS[i] == 1): PgS[i] = Ply
        elif(GS[i] == 5): PgS[i] = Bot
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


def MyPick(GS):
    try:
        che = int(input("Pick an Empty Slot: "))
        if(che >= 1 and che <= 9 and GS[che-1] == 0):
            print(f"You Picked Box: {che}")
        else:
            print("Wrong choice, Picking random since ure so dumb :P")
            while(GS[che-1] != 0): che = random.randint(1,9)
        #GS[che-1] = 1
    except:
        print("Wrong choice, Picking random since ure so dumb :P")
        che = random.randint(1,9)
        while(GS[che-1] != 0): che = random.randint(1,9)
        #GS[che-1] = 1
    
    return che


def PlaceMark(GS, is_Ply_Turn, Pick):
    if(is_Ply_Turn):
        GS[Pick-1] = 1
    else: 
        GS[Pick-1] = 5
    return


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
    is_Ply_Turn = True
    Ply = ""
    Bot = ""

    print("Lets Play a Game!")
    ch = int(input("Choose 1 for X and 2 for O: "))

    match ch:
        case 1:
            Ply = "X"
            Bot = "O"
        case 2:
            is_Ply_Turn = False
            Ply = "O"
            Bot = "X"
        case _:
            print("Wrong Choice picked!, Giving Default pick: 1")
            Ply = "X"
            Bot = "O"

    diff = input("Choose Difficulty(Easy/Med/Hard): ").capitalize()
    try:
        BotPkFn = getattr(SB, f"BotPick_{diff}")
    except:
        print("Typo!....defaulting to Easy")
        BotPkFn = getattr(SB, "BotPick_Easy")
    
    
    print("Lets Start Shall we!")
    print(f"You chose {Ply}")


    while(GameEnded == 0):
        PrintGameState(GameState, Ply, Bot)
        Pick = 0
        if(is_Ply_Turn): 
            print("Your Turn")
            Pick = MyPick(GameState)
        else:
            print("Bot's Turn")
            Pick = BotPkFn(GameState)

        PlaceMark(GameState, is_Ply_Turn, Pick)
        
        is_Ply_Turn = not is_Ply_Turn    
        GameEnded = HasEnded(GameState)



    PrintGameState(GameState, Ply, Bot)
    print("------GAME OVER------")


    if(GameEnded == 2): print("The Game was a DRAW!")
    elif(GameEnded == 5): print(f"Bot won :( as {Bot}")
    elif(GameEnded == 1): print(f"You Won! as {Ply}")
    print("Hope You Enjoyed :)")


if(__name__ == "__main__"):
    main()
