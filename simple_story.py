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
    print("""One day you and a group of friends went hiking. At camp you wanted to see the animals in the area.
    When you came back to check on the camp you saw that everyone had left without you.
    You were confused but you took up the supplies you still had and tried to find them.
    As you walked the trail disappeared from behind you and you realized you were lost.
    So can you escape the forest?""")

    ask_q("You start to get hungry as you walk the path you spot an apple tree and a bush with some type of berry you can't identify", 4, "Pick an apple and eat it", "Grab a handful of berries", "Walk past and try to find more food", "Go hunting to find food")

    if choice == "1":
        print("""You pick the apple off the tree and take a big bite. You feel satisfied after being hungry for so long, but you start to feel sick.
        It gets worse until you fall to the ground. Looking at the apple in your hand, you spot mold inside.
        YOU LOSE""")
        return

    elif choice == "2":
        print("You pick a handful of berries. They don't taste the best, but you find enough edible ones to satisfy your hunger.")

    elif choice == "3":
        print("""You walk past the tree and the bush. After a while, you can't find any more food. You fall from starvation.
        YOU LOSE""")
        return

    else:
        ask_q("You chose to go hunting. You can hunt with a spear or set up a trap.", 2, "Make a spear", "Build a trap", "", "")

        if choice == "1":
            print("You fashion a spear from a sturdy branch and manage to catch a small rabbit.")

        else:
            print("You set up a trap and wait. After a while, you catch a small squirrel.")

        ask_q("Do you cook the meat or eat it raw?", 2, "Cook", "Eat it raw", "", "")

        if choice == "1":
            print("""You go to collect kindling, leaving the meat behind. When you return, you can't find it. Some other animal has probably taken it.""")

            ask_q("You can hunt again, but you also see a log that has bugs underneath it.", 2, "Hunt again", "Eat the bugs", "", "")

            if choice == "1":
                print("You hunt again and don't make the same mistake. You cook the meat and satisfy your hunger.")

            else:
                print("You overturn the log and eat some bugs. They taste disgusting, but you feel fine and satisfy your hunger.")

        else:
            print("""You eat the raw meat. Soon, you start feeling sick. Your stomach hurts, and you collapse.
            YOU LOSE""")
            return

    print("\nYou continue walking through the forest, feeling a little stronger now.")

    ask_q("You reach a fork in the path. You hear rushing water to your left and see smoke rising in the distance to your right.", 3, "Follow the sound of water", "Head toward the smoke", "Climb a tree to look around", "")

    if choice == "1":
        print("You follow the sound of water until you reach a river.")

        ask_q("The river is wide. How will you cross?", 3, "Swim across", "Look for a shallow crossing", "Follow the river downstream", "")

        if choice == "1":
            print("""You jump into the river, but the current is much stronger than you expected. You struggle to stay above the water and are swept away.
            YOU LOSE""")
            return

        elif choice == "2":
            print("After searching for a while, you find a shallow crossing between some rocks and carefully make your way across.")

        else:
            print("You follow the river downstream until you discover a small wooden bridge and cross safely.")

    elif choice == "2":
        print("You walk toward the smoke and discover an abandoned campsite.")

        ask_q("There is a backpack beside a cold fire. What do you do?", 3, "Search the backpack", "Try to restart the fire", "Ignore the camp and keep walking", "")

        if choice == "1":
            print("Inside the backpack, you find a map, a compass, and a bottle of water. The map shows a road nearby.")

        elif choice == "2":
            print("You use some dry wood to restart the fire. The smoke rises high above the trees, making you easier to spot.")

        else:
            print("You leave the campsite behind and continue through the trees.")

    else:
        print("You climb a tall tree and spot a distant road beyond the forest. You climb down carefully and head in that direction.")

    print("\nAs evening approaches, you realize that you need to find somewhere safe to spend the night.")

    ask_q("You see a cave and a large tree with thick branches. Where will you sleep?", 3, "Sleep inside the cave", "Climb into the tree", "Keep walking through the dark", "")

    if choice == "1":
        print("You enter the cave and hear strange noises coming from deep inside.")

        ask_q("Something is moving in the darkness. What do you do?", 2, "Run out of the cave", "Stay quiet and slowly back away", "", "")

        if choice == "1":
            print("""You sprint out of the cave and trip over a rock, badly hurting your leg. You cannot travel far enough to escape.
            YOU LOSE""")
            return

        else:
            print("You quietly back away and leave the cave. Whatever was inside never notices you.")

    elif choice == "2":
        print("You carefully climb into the tree and find a sturdy branch to rest on. You survive the night.")

    else:
        print("""You keep walking through the darkness. You trip over roots and lose your way completely.
        Exhausted and unable to see, you cannot find your way out.
        YOU LOSE""")
        return

    print("\nThe next morning, you wake up to the sound of birds and distant engines.")

    ask_q("You finally reach a road. A car is approaching, but you also see a trail leading toward a nearby building.", 3, "Wave down the car", "Follow the trail to the building", "Hide and wait for your friends", "")

    if choice == "1":
        print("""You wave your arms, and the driver notices you. The car stops, and the driver offers to take you to the nearest ranger station.
        You explain what happened, and the rangers help you contact your friends.
        YOU WIN! YOU ESCAPED THE FOREST!""")

    elif choice == "2":
        print("""You follow the trail and discover a forest ranger station. You knock on the door, and a ranger comes outside.
        You explain that you got lost, and the ranger helps you get back to safety.
        YOU WIN! YOU ESCAPED THE FOREST!""")

    else:
        print("""You wait beside the road, hoping your friends will return. Hours pass, and nobody comes.
        As night approaches, you realize that waiting was a mistake.
        YOU LOSE""")
        return

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



