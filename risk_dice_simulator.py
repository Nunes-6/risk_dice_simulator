import random

game_end = "n"

while game_end != "y":

    #declaring variables
    max_attacks = int(input("Number of attacking troops: ")) #rules say it caps out at 3
    max_def = int(input("Number of defending troops: "))
    attacking_troops = max_attacks
    defending_troops = max_def
    att_roll = [0,0,0]
    def_roll = [0,0]
    att_score = 0
    def_score = 0

    while (attacking_troops != 0) and (defending_troops != 0):

        #rolling all attacking dice
        for i in range(0,3):
            att_roll[i] = random.randint(1,6)

        #choosing attacking score
        att_score = max(att_roll[:min(3,attacking_troops)])

        #rolling all defending dice
        for i in range(0,2):
            def_roll[i] = random.randint(1,6)

        #choosing defending score
        if defending_troops < 3:
            def_score = def_roll[0]
        else:
            def_score = max(def_roll)

        #establishing who loses troops
        if att_score > def_score:
            defending_troops -= 1
        else:
            attacking_troops -= 1


    print("Attacking troops remaining: "+str(attacking_troops))
    print("Defending troops remaining: "+str(defending_troops))
    game_end = input("Would you like to end the game? (y/n) ")
