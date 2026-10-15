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
    print("""You are a sailor searching for a legendary treasure that supposedly lies hidden on a mysterious island.
    After months of searching, you finally discover an old map inside a bottle.
    The map shows an island with an X marking the location of the treasure.
    You gather your supplies, board your small boat, and sail toward the island.
    But finding the treasure won't be easy.
    Can you find the treasure and escape the island alive?""")

    ask_q("You arrive at the island and see a jungle, a rocky mountain, and a beach cave. Where do you explore first?", 3, "Explore the jungle", "Climb the mountain", "Enter the beach cave", "")

    if choice == "1":
        print("You enter the thick jungle. After walking for a while, you discover an old wooden sign pointing deeper into the forest.")

        ask_q("You hear strange noises coming from the bushes. What do you do?", 3, "Investigate the noises", "Follow the wooden sign", "Climb a tree to look around", "")

        if choice == "1":
            print("""You walk toward the bushes and suddenly a wild boar charges at you.
            You try to run, but you trip over a root.
            YOU LOSE""")
            return

        elif choice == "2":
            print("You follow the sign and discover an abandoned pirate camp. Inside a broken chest, you find a rusty key.")

        else:
            print("You climb a tree and spot a stone temple hidden deeper in the jungle. You climb down and head toward it.")

    elif choice == "2":
        print("You begin climbing the rocky mountain. The climb is difficult, but from the top you can see the entire island.")

        ask_q("You spot a waterfall and a ruined temple below. Which way do you go?", 2, "Go toward the waterfall", "Head toward the temple", "", "")

        if choice == "1":
            print("Behind the waterfall, you discover a small opening in the rock. Inside, you find an old pirate skeleton holding a rusty key.")

        else:
            print("You reach the ruined temple and find strange symbols carved into the stone walls.")

    else:
        print("You enter the dark cave. You notice footprints in the sand and an old wooden chest near the back.")

        ask_q("The cave gets darker as you go deeper. What do you do?", 2, "Open the wooden chest", "Search the cave walls", "", "")

        if choice == "1":
            print("""You open the chest, but it is a trap. A pile of rocks falls from above and blocks the entrance.
            You cannot escape the cave.
            YOU LOSE""")
            return

        else:
            print("You discover a hidden passage behind some rocks. At the end, you find a rusty key and an old note.")

    print("\nYou continue your search for the treasure.")

    ask_q("You find three paths leading away from the area. One leads to a stone temple, one to a swamp, and one to a wooden bridge.", 3, "Enter the stone temple", "Cross the swamp", "Cross the wooden bridge", "")

    if choice == "1":
        print("You enter the temple and discover a stone door with a keyhole.")

        ask_q("You have found a strange door. How do you open it?", 2, "Use the rusty key", "Force the door open", "", "")

        if choice == "1":
            print("The key fits perfectly! The door slowly opens, revealing a room filled with ancient paintings and a staircase leading underground.")

        else:
            print("""You push against the stone door, but the ceiling begins to collapse.
            You are buried under the falling rocks.
            YOU LOSE""")
            return

    elif choice == "2":
        print("You step into the swamp. The water is muddy, and the ground is unstable.")

        ask_q("You notice a fallen tree and a narrow path through the water. Which do you use?", 2, "Walk across the fallen tree", "Take the narrow path", "", "")

        if choice == "1":
            print("You carefully cross the fallen tree and discover a stone door hidden among the trees.")

        else:
            print("""You step onto a patch of soft mud and sink deeper and deeper.
            You cannot pull yourself free.
            YOU LOSE""")
            return

    else:
        print("You carefully cross the wooden bridge. Halfway across, a plank breaks beneath your foot.")

        ask_q("The bridge starts falling apart. What do you do?", 2, "Jump to the other side", "Turn around and go back", "", "")

        if choice == "1":
            print("You make a desperate leap and land safely on the other side. Nearby, you discover a stone door.")

        else:
            print("You slowly make your way back and find another path leading to the stone door.")

    print("\nYou finally reach a huge stone door covered in pirate symbols.")

    ask_q("The door opens, revealing two tunnels. One has golden coins scattered on the floor, while the other has an X carved into the wall.", 2, "Follow the golden coins", "Follow the X symbol", "", "")

    if choice == "1":
        print("""You follow the golden coins into a narrow tunnel. Suddenly, the ground gives way beneath you.
        You fall into a deep pit filled with sharp rocks.
        YOU LOSE""")
        return

    else:
        print("You follow the X symbols until you reach a massive underground chamber.")

    print("\nInside the chamber, you see a giant treasure chest sitting on a stone platform.")

    ask_q("The treasure chest is surrounded by traps. How will you reach it?", 3, "Run straight to the chest", "Look for a safe path", "Throw a rock to test the floor", "")

    if choice == "1":
        print("""You rush toward the chest, but the floor triggers a trap. Arrows shoot from the walls.
        You fall before reaching the treasure.
        YOU LOSE""")
        return

    elif choice == "2":
        print("You carefully examine the floor and spot several pressure plates. You step around them and safely reach the chest.")

    else:
        print("You throw a rock onto the floor. Several hidden traps activate, revealing which stones are safe. You carefully cross the chamber.")

    print("\nYou stand in front of the treasure chest. It has a large lock.")

    ask_q("How will you open the chest?", 3, "Use the rusty key", "Smash the lock with a rock", "Search the chamber for clues", "")

    if choice == "1":
        print("You insert the rusty key. It turns with a loud click, and the chest opens!")

    elif choice == "2":
        print("""You smash the lock, but the chest triggers a hidden trap. Poisonous gas fills the chamber.
        You collapse before you can escape.
        YOU LOSE""")
        return

    else:
        print("You search the walls and discover a hidden lever. You pull it, and the chest unlocks with a loud click!")

    print("""\nYou slowly open the chest. Inside are piles of gold coins, sparkling jewels, and a golden crown.
    At the bottom, you find a note written by the pirate who hid the treasure.
    It says that anyone who finds the treasure may claim it as their own.
    YOU FOUND THE TREASURE!""")

    ask_q("You have the treasure, but the island is beginning to shake as the ancient chamber collapses. What do you do?", 2, "Grab as much treasure as possible and run", "Forget the treasure and escape immediately", "", "")

    if choice == "1":
        print("""You grab a heavy bag of gold and race toward the exit.
        The extra weight slows you down, and rocks fall around you.
        You barely make it outside with the treasure just before the chamber collapses.
        You rush to your boat and sail away with your fortune.
        YOU WIN! YOU FOUND THE LOST PIRATE TREASURE!""")

    else:
        print("""You leave the treasure behind and sprint toward the exit.
        You escape the collapsing chamber and reach your boat safely.
        Although you leave the gold behind, you survive the adventure.
        YOU SURVIVED, BUT THE TREASURE REMAINS ON THE ISLAND!""")
def sea_voyage():
    print("""You are a sailor on a voyage across the ocean.
    One night, a massive storm hits your ship. The waves crash against the deck,
    the sails tear apart, and your compass falls into the sea.
    When the storm finally passes, you discover that you are far from your planned route.
    Your ship is damaged, your supplies are limited, and you have no idea where you are.
    Can you navigate your way back home?""")

    ask_q("You inspect your ship and realize you need to act quickly. What do you do first?", 3, "Repair the sails", "Check the navigation equipment", "Search for food and water", "")

    if choice == "1":
        print("You manage to repair part of the sails using spare rope and cloth. Your ship can move again.")
    elif choice == "2":
        print("You check the navigation equipment, but your compass is broken and your map is soaked.")
    else:
        print("You search the storage room and find a few cans of food and several bottles of water.")

    print("\nThe next morning, you notice something floating in the water nearby.")

    ask_q("You spot a wooden crate, a group of dolphins, and a distant island. What do you investigate?", 3, "Retrieve the wooden crate", "Follow the dolphins", "Sail toward the island", "")

    if choice == "1":
        print("You pull the crate aboard. Inside, you find a working compass and a small waterproof map.")
        compass = True
    elif choice == "2":
        print("You follow the dolphins for a while. They lead you toward a region where seabirds are flying, suggesting land may be nearby.")
        compass = False
    else:
        print("You sail toward the island and discover a small beach where you can rest.")
        compass = False

    print("\nAs the day continues, dark clouds begin gathering on the horizon.")

    ask_q("Another storm is approaching. How will you prepare?", 3, "Lower the sails and secure everything", "Keep sailing at full speed", "Anchor the ship and wait", "")

    if choice == "1":
        print("You lower the sails and secure the loose equipment. Your ship rides out the storm safely.")
    elif choice == "2":
        print("""You keep sailing at full speed, but a powerful wave slams into the ship.
        Water floods the deck, and your ship begins to sink.
        YOU LOSE""")
        return
    else:
        print("You drop the anchor, but the ocean is too deep. The anchor cannot reach the seabed, and the ship drifts during the storm.")

    print("\nAfter the storm, you notice a flock of seabirds flying in one direction.")

    ask_q("You need to figure out where land is. What do you do?", 3, "Follow the seabirds", "Sail toward the setting sun", "Stay where you are and wait", "")

    if choice == "1":
        print("You follow the seabirds and eventually spot land on the horizon.")
    elif choice == "2":
        print("You sail west toward the setting sun, hoping it will lead you home. After hours of sailing, you see a large cargo ship in the distance.")
    else:
        print("""You wait for help, but nobody appears.
        Your food and water begin running low, and you become too weak to continue.
        YOU LOSE""")
        return

    print("\nYou have found a possible route to safety, but you still need to navigate carefully.")

    if compass:
        ask_q("You check your compass and map. They suggest two possible routes home. Which do you choose?", 2, "Take the shorter route through a narrow channel", "Take the longer route through open water", "", "")

        if choice == "1":
            print("You steer toward the narrow channel, but strong currents push your ship toward dangerous rocks.")

            ask_q("The ship is drifting toward the rocks. What do you do?", 2, "Turn sharply away from the rocks", "Keep going and hope to pass", "", "")

            if choice == "1":
                print("You turn the wheel just in time and steer into safer water.")
            else:
                print("""Your ship strikes the rocks and begins taking on water.
                You cannot repair the damage in time.
                YOU LOSE""")
                return
        else:
            print("You choose the longer route through open water. It takes more time, but the sailing conditions are safer.")

    else:
        ask_q("You have no reliable compass. How will you navigate?", 3, "Use the stars at night", "Follow the coastline of the island", "Sail randomly and hope for the best", "")

        if choice == "1":
            print("That night, you use the North Star to estimate your direction and adjust your course.")
        elif choice == "2":
            print("You follow the coastline until you discover a fishing boat near a small harbor.")
        else:
            print("""You sail without a plan and become hopelessly lost again.
            Your fuel and supplies run out before you find land.
            YOU LOSE""")
            return

    print("\nAfter several more hours, you see a ship approaching.")

    ask_q("The ship is getting closer. How do you get its attention?", 3, "Fire a signal flare", "Wave a bright piece of cloth", "Ignore it and keep sailing", "")

    if choice == "1":
        print("You fire a signal flare into the sky. The crew notices it and changes course toward you.")
    elif choice == "2":
        print("You wave the bright cloth above your head. A sailor spots you and signals back.")
    else:
        print("""You ignore the ship, thinking you can find your own way home.
        Soon, it disappears over the horizon.
        You continue sailing, but your supplies run out.
        YOU LOSE""")
        return

    print("\nThe other ship comes alongside yours, and its captain offers to help.")

    ask_q("The captain offers you two options. What do you choose?", 2, "Accept a tow to the nearest harbor", "Ask for a map and navigate home yourself", "", "")

    if choice == "1":
        print("""The captain attaches a towline to your ship and guides you safely to the nearest harbor.
        You step onto land, exhausted but relieved.
        YOU WIN! YOU MADE IT BACK TO SAFETY!""")
    else:
        print("""The captain gives you a map and helps you determine your position.
        You set your course, follow the map, and sail carefully through the remaining waters.
        After days at sea, you finally recognize the coastline of your home.
        You sail into the harbor as people cheer from the docks.
        YOU WIN! YOU NAVIGATED YOUR WAY HOME!""")
end = "no"
while end == "no":
    ask_q("Which Story Experience do you want?", 3, "Forest Escape", "Treasure Island", "Sea Voyage", "")
    if choice == "1":
        forest_escape()
    elif choice == "2":
        treasure_island()
    else: 
        sea_voyage()
    ask_q("Play another game?", 2, "yes", "no","","")
    if choice == "2":
        end = "yes"
#is it good?