def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You call up a local wizard to inspect the obviously magical sword, because you have no idea what kind of magics could be at work.")
    print("The wizard tells you that the sword was very cursed, but they have removed the curse and now you are left a sword that would fetch quite a high price with collectors!")
    print("You end up selling the sword for a high price to a extremely wealthy noble, leaving you and your family very well off!")
    print("You have ensured good lives for you and your family while also ridding the world of a cursed sword.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You make your own path and cut through the brush. You become lost to the forest.")

if __name__ == "__main__":
    intro()
