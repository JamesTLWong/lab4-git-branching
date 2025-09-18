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

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You accept, but noticing you are unarmed the squirrl leads you to a glowing sword in a stone")
    print("Confused by why you would need a sword to fight a squirrel, you nevertheless accept the gesture and try to pull the sword from the stone")
    print("As soon as you grab the handle a loud cackle bursts through your mind. The sword was cursed! And now so are you!")
    print("Your body is no longer your own, the curse's plan to use the squirrel that touched it to lure in a human worked")
    print("The curse uses your body to wreak havoc on innocents until someone finally stops you")
    print("The last thing you see is a wizard standing over you, shaking their head, saying 'tsk, what a shame, I hope this poor fool can at least rest now")

def center_path():
    print("You make your own path and cut through the brush. You become lost to the forest.")

if __name__ == "__main__":
    intro()
