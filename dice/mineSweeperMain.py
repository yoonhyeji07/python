import mineSweeperField
import mineSweeperSQL
import time
from random import randint

while True:
    print("You've entered my mineField!\n")
    time.sleep(2)

    print("1. login")
    print("2. register")
    print("3. quit")
    action = input("\nChose your action!")

    player = mineSweeperSQL.PlayerToServer()
    data = ()

    if action == '1':
        inputID = input("Input ID : ")
        inputPW = input("Input PW : ")
        data = (inputID, inputPW)
        player.login2(data)

    elif action == '2':
        inputID = input("Input ID : ")
        inputPW = input("Input PW : ")
        inputPW2 = 'Hard-coding Bug!! Simple, but effective!'
        data = (inputID, inputPW)
        time.sleep(1)

        while not inputPW == inputPW2:
            inputPW2 = input("(Re)Input PW : ")
        player.register(data)

    elif action == '3':
        print("Alright.. get the hell outta here you coward!")
        time.sleep(1)
        break

    else:
        print("Interesting... Never expected kinda input... I'm gonna kick your ass outta here!")
        time.sleep(1)
        break

    print("In order to get out of here,")
    print("you should figure out how many mines i've mined!\n")
    time.sleep(4)
    print("Number on the field represents how many mines are near that number")
    print("including diagonal directions.\n")
    time.sleep(4)
    print("Good Luck to your brain!\n")
    time.sleep(2)

    input_1 = int(input("Input size of field : "))
    index_ = randint(1, input_1)
    mineSweeperField.index_ = index_

    mineSweeperField.MineSweeper.createMineField(input_1, index_)
    print(index_)  # Just for cheating...

    print("I'll give you some time...\n")
    time.sleep(2)
    print("Do your best!")
    time.sleep(index_)

    print("Okay, enough thinking time!\n")
    time.sleep(2)
    print("How many mines i've buried?\n")
    time.sleep(2)

    input_2 = int(input("Buried mines : "))
    print(data)  # Check data

    if input_2 == index_:
        print("Darn it!! '%s' is correct!!" % input_2)
        print("I'll let you go for this time...\n")
        time.sleep(4)
        player.winCount()

    else:
        print("Ha..Ha..Ha... well well...\n")
        time.sleep(2)
        print('''That is "W-R-O-N-G" answer..\n''')
        time.sleep(2)
        print("I'll take your brain for being useless!")
        time.sleep(2)
        print("G A M E O V E R")
        print("press any key to return to main menu\n")
        time.sleep(4)
        player.lostCount()