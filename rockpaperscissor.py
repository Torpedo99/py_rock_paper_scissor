from random import randint
def cpuChoose():
    return randint(1,3)
def round(s1, s2):
    choiceString = input("Enter rock/paper/scissor ")
    cpu = cpuChoose()
    if(choiceString.lower() == "rock"):
        if(cpu == 1):
            print("CPU chooses Rock!")
            print("Draw!")
        elif(cpu == 2):
            print("CPU chooses Paper!")
            print("CPU gains a Point!")
            s2 += 1;
        elif(cpu == 3):
            print("CPU chooses Scissor!")
            print("You gain a Point!")
            s1 += 1
    if(choiceString.lower() == "paper"):
        if(cpu == 1):
            print("CPU chooses Rock!")
            print("You gain a Point!")
            s1 += 1;
        elif(cpu == 2):
            print("CPU chooses Paper!")        
            print("Draw!")
        elif(cpu == 3):
            print("CPU chooses Scissor!")
            print("You lost a Point!")
            s2 += 1
    if(choiceString.lower() == "scissor"):
        if(cpu == 1):
            print("CPU chooses Rock!")
            print("You lost a Point!")
            s2 += 1
        elif(cpu == 2):
            print("CPU chooses Paper!")
            print("You gain a Point!")
            s1 += 1;
        elif(cpu == 3):
            print("CPU chooses Scissor!")
            print("Draw")
    print("Your Score: " + str(s1) + "  |  " + "CPU Score: " + str(s2))
    print("-----------------------------------------")    
    if(s1 == 3):
        print("You have won the game!");
        print("*************************************")
        return
    if(s2 == 3):
        print("You have lost the game!")
        print("*************************************")
        return
    round(s1, s2)  
round(0, 0)
