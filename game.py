def print_win_message(word):
    win_message = (f"Congrats, you won! The word is: {word}")
    print(win_message)

def print_lose_message(word):
    lose_message = f"Sorry you lost. The word is: {word}"
    print(lose_message)


def print_status(progress, wrong_letters, num_of_guesses):

    word = f"Word: {progress}"
    guess_remaining = f"Guesses Remaining: {num_of_guesses}"
    wrong = f"Wrong: {wrong_letters}"

    print(word)
    print(guess_remaining)
    print(wrong)


def get_user_guess():

    while True:
        user_guess = input("Guess a letter:  ").lstrip()
        if len(user_guess) == 1 and user_guess.isalpha():
            return user_guess
        else:
            print("You must guess a single letter!")

def update_progress(word, progress, guess):
    new_progress = list(progress)

    for letter in range(len(word)):
        if word[letter] == guess:
            new_progress[letter] = guess

    update = ""
    for letters in new_progress:
        update = update + letters
        return update


