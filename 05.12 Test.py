from random import randint
randomNum= randint(1,20)
WinFlag=False
for i in range(1,4): ##3 Tries
    GuessedNum = input("Guess the Number(from 1 to 20):")
if GuessedNum == randomNum:
    WinFlag=True
    #break
elif GuessedNum>randomNum:
    print("Your guess is too high...")
elif GuessedNum<randomNum:
    print("Your guess is too low...")
##Winner
if WinFlag==False :
    print("\nComputer Win!!!")
else:
    print("\nCorrect guess...You Win!!!")