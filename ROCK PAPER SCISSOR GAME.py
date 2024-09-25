import random
l=["ROCK","SCISSOR","PAPER"]
while True:
    Ccount=0
    Ucount=0
    uc=int(input(
        '''
        GAME START
        1.YES..
        2.NO/EXIT..
        '''))
    if(uc==1):
        for a in range(1,6):
            userInput=int(input(
                '''
                1.ROCK
                2.SCISSOR
                3.PAPER
                '''))
            if(userInput==1):
                uchoice="ROCK"
            elif (userInput==2):
                uchoice="SCISSOR"
            elif(userInput==3):
                uchoice="PAPER"
            Cchoice=random.choice(l)
            '''
            print(uchoice)
            print(cchoice)'''
            if(Cchoice==uchoice):
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Game drow")
                Ucount=Ucount+1
                Ccount=Ccount+1                
            elif(uchoice=="ROCK"and Cchoice=="SCISSOR")or(uchoice=="PAPER"and Cchoice=="ROCK")or(uchoice=="SCISSOR"and Cchoice=="PAPER"):
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("YOU WIN")
            else:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("COMPUTER WIN")
                Ccount=Ccount+1
            if(Ucount==Ccount):
                print("FINAL GAME DRAW")
                print("USERSCOER",Ucount)
                print("COMPUTERCOER",Ccount)
            elif(Ucount>Ccount):
                print("FINAL YOU WIN THE GAME")
                print("USERSCOER",Ucount)
                print("COMPUTERCOER",Ccount)
            else:
                print("FINAL COMPUTER WIN THE GAME")
                print("USERSCOER",Ucount)
                print("COMPUTERCOER",Ccount)
                
                
                
                
                