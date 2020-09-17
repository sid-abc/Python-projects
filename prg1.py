
# Simple game

print("WELCOME!")
name = input("what is your name ")
age = int(input("What is your age? "))
health = 10

if age >= 12:
    print("Hello " + name + " are old enough to play!")
    
    wants_toplay = input("Are you ready to play? ").lower()
    if wants_toplay == "yes":
        print("You are starting with " + str(health) + " health")
        print("Let's play!\n")
        left_right = input("You are in a forest. There are two ways to go.....Left way or right way (left/right)?  ").lower()
        if left_right == "right":
            ans = input("Nice, you follow the path and reach a lake...Do you swim accross or go around (swim/around)?  ").lower()

            if ans == "around":
                print("You went around and reached other side of lake.")
            elif ans == "swim":
                print("You managed to swim, but got bitten by fish and lost -5 heath.")
                health -= 5
            ans = input("You notice a house and a river. Which do you go to (river/house)?  ").lower()
            if ans == "house":
                print("You enter the house but get attacked by a thief....You lose -5 health")
                health -= 5

                if health <= 0:
                    print("You  now have 0 heath and have lost the game...")
                else:
                    print("You have survived... You win!")
            elif ans == "river":
                print("You get rescued and have survived... YOU WIN !!")
        else:
            print("You fell down and lost")
    else:
        print("See you later")    
else:
    print("You are not old enough to play")