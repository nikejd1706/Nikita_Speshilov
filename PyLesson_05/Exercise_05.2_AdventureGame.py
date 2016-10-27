print("We are going on an adventure!")
adventure = int(input("You walk into the forest, do you go..." +
                        "\n 1. left " +
                        "\n 2. right "))
if adventure == 1:
    adventure = int(input("You encounter a demon, how do you proceed....?" +
                       "\n 1. ignore it" + 
                       "\n 2. attack it"))
    if adventure == 1:
        print("You kept walking and encounter a bridge. Continue or go around?")
        print(" 1. continue onward!" + "\n 2. go around slowly")
        adventure = int(input("what do you choose?"));
        if adventure == 1:
            print("You walk on the bridge and see a clown. He has a gun and shoots you in the heart.")
            
        else:
            print("You go around and see a volcano errupt in the distance. Lava flies and falls on you and you die.")
    else:
        adventure = int(input("You see a rock to the left and an axe father ahead. What do you get?"))
        print(" 1. rock" + "\n 2. axe")
        if adventure == 1:
            print("You throw the rock at it, but it blocks it back and hits you in the head. You pass out and it possesses you.")
        else:
            print("You run to get the axe, but the demon grabs it first and cuts a tree which falls on you.")
else:
    adventure = int(input("You walk up to a river, do you...." +
             "\n 1. Attempt to build a boat" +
             "\n 2. Swim through it"))
    if adventure == 1:
        print("You start building a boat out of natural resources, do you use wood or stone?")
        adventure = int(input(" 1. wood" + "\n 2. stone"))
        if adventure == 1:
            print("You assemble the boat using wood. You go into the water and everything is fine until a Megaladon jumps out and devours you!")
        else:
            print("You start picking out and mining stones. You realize that you don't have any water. You die of heat exhaustion a few hours later.")
        

    else:
        adventure = int(input("You are trying to decide if you should swim....." +
                              "\n 1. underwater" +
                              "\n 2. on top of water"))
        if adventure == 1:
            print("You start swimming through the river. Everything is okay until you feel something is touching you. You look down and see blood-sucking leeches coming toward you to feast on you. You give up and drown.")
        else:
            print("You are halfway through the river when you hear a bird. You look up and there's a massive vulture coming at you. You don't have any time to think so the vulture lifts you by your neck and chokes you.")
            
            
