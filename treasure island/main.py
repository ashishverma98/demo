print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print("WELCOME TO THE TREASURE ISLAND")

direction = input("right or left? ")
if direction == "left":
    swim_wait = input("wait or swim? ")
    if swim_wait == "wait":
        door = input("which door you want to choose red yellow or blue? ")
        if door == "yellow":
            print("you win")
        else:
            print("game over! you loose!")
    else:
        print("game over! you loose!")
else:
    print("game over! you loose!")
    