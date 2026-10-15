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
    print("hello")
def treasure_island():
    print("hello")
def sea_voyage():
    print("hello")
name = input("Hi welcome to the story game, whats your name?   ")

ask_q(f"Hi {name}! Which Story Experience do you want?", 3, "Forest Escape", "Treasure Island", "Sea Voyage", "")
if choice == 1:
    forest_escape()
elif choice == 2:
    treasure_island()
else: 
    sea_voyage()



