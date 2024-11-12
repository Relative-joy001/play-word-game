import game
import random



with open ("words.txt", "r") as file:
    content = file.readlines()

def chose_random_word():
    list_of_words = content
    word_chosen = random.choice(list_of_words)
    return word_chosen

while True:
    random_word = chose_random_word()
    num_of_guesses = 4 + len(random_word)

    game.play_word_game(random_word, num_of_guesses)

    play_again = input("Do you wish to play again[type 'yes' or 'no']: ")

    if play_again == "yes":
        continue
    else:
        print("Thanks for plkaying!!")
        break
