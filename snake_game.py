name=str(input("Enter your Name : "))
print("Hello",name,"!! Welcome to Snake_Ladder !!")
print("Powered by B3 - E&TC and Electrical")
print("Co-Powered By Shikhuyaa..")
print()
player=0
while player < 100:
    try:
        dice=int(input("Enter Count: "))
    except Exception as dicee:
        print(dicee)
    else:
        if player == 95 and dice>5:
            print("Try Again..")
        elif player == 96 and dice>4:
            print("Try Again..")
        elif player == 97 and dice>3:
            print("Try Again..")
        elif player == 98 and dice>2:
            print("Try Again..")
        elif player == 99 and dice>1:
            print("Try Again..")
        else:
            if dice<=0 or dice>6:
                print("Invalid Count , Try Again")
            else:
                player = player + dice
                if player == 99:
                    player = 8
                    print("Ohh God !! Snake Bite..")
                if player == 92:
                    player = 21
                    print("Ohh God !! Snake Bite..")
                if player == 75:
                    player = 39
                    print("Ohh God !! Snake Bite..")
                if player == 61:
                    player = 2
                    print("Ohh God !! Snake Bite..")
                if player == 44:
                    player = 22
                    print("Ohh God !! Snake Bite..")
                if player == 6:
                    player = 30
                    print("Ladder Found..")
                if player == 19:
                    player = 64
                    print("Ladder Found..")
                if player == 77:
                    player = 94
                    print("Ladder Found..")
                if player == 48:
                    player = 83
                    print("Ladder Found..")
                print("Player Position is",player)
                if player == 100:
                    print("Congratulations..!!\n7 Crore..")
