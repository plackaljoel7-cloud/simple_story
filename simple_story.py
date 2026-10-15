choice = ""
def ask_q(text, count, one, two, three, four):
    global choice
    valid = ""
    while valid != "yes":
        if count == 2:
            choice = input(f"""{text}
            Option 1: {one}
            Option 2: {two}
            Type a Number 1-2
            Choice:   """)
        elif count == 3:
            choice = input(f"""{text}
            Option 1: {one}
            Option 2: {two}
            Option 3: {three}
            Type a Number 1-3
            Choice:   """)
        else:
            choice = input(f"""{text}
            Option 1: {one}
            Option 2: {two}
            Option 3: {three}
            Option 4: {four}
            Type a Number 1-4
            Choice:   """)
        if choice in ("1","2","3","4") and count == 4 or choice in ("1","2","3") and count == 3 or choice in ("1","2") and count == 2:
            valid = "yes"
        else:
            print(f"That is Not Valid, Type a Number 1-{count}")
def forest_escape():
    print("""One day you and a group of friends went hiking. at camp you wanted to see the animals in the area.
    When you came back to check on the camp you saw that everyone had left without you.
    You were confused but you took up the supplies you still had and tried to find them.
    As you walked the trail disapeared from behind you and you realized you were lost.
    So can you escape the forest?""")
    ask_q("You start to get hungry as you walk the path you spot an apple tree and a bush with some type of berry you can't identify", 4, "Pick an apple and eat it", "Grab a handful of berry's", "Walk past and try to find more food", "Go hunting to find food")
    if choice == "1":
        print("""You pick the apple of the tree and take a big bite satisfied after being hungry for so long but you feel a little bit sick.
        It gets worse and worse until you fall to the ground looking at the apple that was in your hand and you spot mold inside.
        YOU LOSE""")
    elif choice == "2":
        print("You pick a handful of berrys and it doesnt taste the best but its edible. you fulffill your hunger.")
    elif choice == "3":
        print("""you walk past the tree and the bush. its been a while and you cant find anymore food. You fall from starvation.
        YOU LOSE""")
    else:
        ask_q("You chose to go hunting. you can hunt with a spear or set up a trap", 2, "Make a spear", "build a trap",'','')
        if choice == "1":
            print("you were able to fashion a spear and you killed a small rabbit")
        if choice == "2":
            print("you set up a trap and you just have to wait till a animal gets caught.")
            print("you were able to catch a small squirrel")
        ask_q("Do you cook the meat or eat it raw?",2, "Cook", "Eat it raw", "", "")
        if choice == "1":
            print("""you go to collect kindling leaving the meat behind when you came back you cant find it.
            some other animal has probably taken it. """)
            ask_q("you can hunt again but you also see a log that has bugs underneath it", 2, "hunt again", "eat the bugs","","")
            if choice == "1":
                print("you hunt again and dont make the same mistake, you cook the meat and satiate your hunger")
            elif choice == "2":
                print("you overturn the log but you feel fine and satiate your hunger")
        elif choice == "2":
            print("""you feel sick and fall down
            YOU LOSE""")


def treasure_island():
    print("Sorry This Feature is not coded yet :(")
def sea_voyage():
    print("Sorry This Feature is not coded yet :(")
name = input("Hi welcome to the story game, whats your name?   ")

ask_q(f"Hi {name}! Which Story Experience do you want?", 3, "Forest Escape", "Treasure Island", "Sea Voyage", "")
if choice == "1":
    forest_escape()
elif choice == "2":
    treasure_island()
else: 
    sea_voyage()



