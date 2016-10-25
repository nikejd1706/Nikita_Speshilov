print("We are going on an adventure!")
adventure = int(input("You walk into the forest, do you go..." +
                        "\n 1. left" +
                        "\n 2. right"))

if adventure == 1:
    adventure = int(input("You encounter a demon, how do you proceed....?" +
                       "\n 1. ignore it" + 
                       "\n 2. attack it"))
    if adventure == 1:
        print("you kept walking; you encounter a bridge. continue or go around the chasm?")
        print(" 1. continue onward!" + "\n 2. go around slowly")
        adventure = int(input("what do you choose?"));
        if adventure == 1:
            print("You walk on the bridge and see a clown. He has a gun and shoots you in the heart.")
            
        else:
            print("You go around and see a volcano errupt in the distance. Lava falls on you and you die.")
    else
        adventure = int(input("You see a rock to the left and an axe father ahead. What do you get?"))
        print(" 1. rock" + "\n 2. axe")
        if adventure == 1
            print("You throw the rock at it, but it blocks it back and hits you in the head. You pass out and it possesses you.")
        else
            print("You run to get the axe, but the demon grabs it first and cuts a tree which falls on you.")
else:
    adventure = int(input("You walk up to a river, do you...." +
             "\n 1. Swim through it" +
             "\n 2. Attempt to build a boat"))
    if adventure == 2:
        print("you start building a boat out of natural resources, do you use wood or stone?")
        adventure = int(input(" 1. wood" + "\n 2. stone")
        if adventure == 1:
            print("you build the boat and go out into the water. You hear a sound underwater. A megaladon jumps out and eats you alive!")
        else:
            #
    else:
        print("You start swimming through the river. Everything is okay until you feel something is touching you. You look down and see blood-sucking leeches coming toward you to feast on you. You give up and drown.")
            #
        else:
            #
            
