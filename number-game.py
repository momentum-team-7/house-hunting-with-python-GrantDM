import random

player_one = random.randint(1,10)

player_two = 0

while player_one != player_two:
    player_two = int(input())
    if player_two == player_one:
            player_two = player_one
            print("that's right")
            break
    elif player_two > player_one:
        print("guess lower")
    else:
        print("guess higher")






