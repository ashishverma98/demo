import random
import os


words = [ "ashish" , "anilkumar", "mayadevi"]
chosen_word = random.choice(words)
n=len(chosen_word)

word = []
for letter in chosen_word:
    word+="_"
print(f"{''.join(word)}")

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("make a letter guess: ").lower()
    os.system('cls') 
    for position in range(n):
        letter = chosen_word[position]
        if letter == guess:
            word[position]= guess
  
    if guess in chosen_word:
        print("you guess the right letter")
    
    elif guess in word:
        print("you already guessed that letter")

    print(f"{''.join(word)}")

    if "_" not in word:
        end_of_game = True
        print("you win!")   

    if guess not in chosen_word:
        lives-=1
        print(f"you guess the wrong letter.you lose a life.You are left with {lives} only")
        if lives==0:
            end_of_game = True
            print("you lose!")
