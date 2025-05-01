# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!

import random,sys

print("ROCK, PAPER, SCISSORS")
print("0 Wins, 0 Losses, 0 Ties")

Wins,Losses,Ties = 0,0,0

while True:
    user_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
    if user_move == "q":
        print("quit")
        sys.exit()
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        machine_move = "r"
    elif randomNumber == 2:
        machine_move = "p"
    elif randomNumber == 3:
        machine_move = "s"

    if user_move == "r" and machine_move == "p":
        Wins += 0
        Losses += 1
        Ties += 0
        print(user_move)
        print("ROCK versus...")
        print("PAPER")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))
    elif user_move == "r" and machine_move == "s":
        Wins += 1
        Losses += 0
        Ties += 0   
        print(user_move)
        print("ROCK versus...")
        print("SCISSOR")   
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))

        break;
    elif user_move == "p" and machine_move == "r":
        Wins += 1
        Losses += 0
        Ties += 0
        print(user_move)
        print("PAPER versus...")
        print("ROCK")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))
        break;
    elif user_move == "p" and machine_move == "s":
        Wins += 0
        Losses += 1
        Ties += 0
        print(user_move)
        print("PAPER versus...")
        print("SCISSOR")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))

    elif user_move == "s" and machine_move == "r":
        Wins += 0
        Losses += 1
        Ties += 0
        print(user_move)
        print("SCISSOR versus...")
        print("ROCK")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))

    elif user_move == "s" and machine_move == "p":
        Wins += 1
        Losses += 0
        Ties += 0
        print(user_move)
        print("SCISSOR versus...")
        print("PAPER")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))

        break;
    elif user_move == "s" and machine_move == "s":
        Wins += 0
        Losses += 0
        Ties += 1
        print(user_move)
        print("SCISSOR versus...")
        print("SCISSOR")
        print("")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))
    elif user_move == "r" and machine_move == "r":
        Wins += 0
        Losses +=0
        Ties += 1
        print(user_move)
        print("ROCK versus...")
        print("ROCK")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))
    elif user_move == "p" and machine_move == "p":
        Wins += 0
        Losses += 0
        Ties += 1
        print(user_move)
        print("PAPER versus...")
        print("PAPER")
        print("{} Wins, {} Losses, {} Ties".format(Wins,Losses,Ties))
    


        
        
