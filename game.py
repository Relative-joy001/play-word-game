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


def play_word_game(word, total_guess):

    print("Welcome to Guess a word game.")

    progress = "_" * len(word)
    num_of_guesses = total_guess
    wrong_letters = ""

    while total_guess > 0:
        game_status = print_status(progress, wrong_letters, total_guess)

        guessed_letters = get_user_guess()

        if guessed_letters in progress or guessed_letters in wrong_letters:
            print("You have already guessed the letter {guessed_letter}. Pick a different letter.")
            continue

        if guessed_letters in word:
            total_guess -= 1
            progress = update_progress(word, progress, guessed_letters)
            
        if guessed_letters not in word:
            total_guess -= 1
            wrong_letters += guessed_letters

        if progress == word:
            print_win_message(word)
            break
        elif progress != word and total_guess == 0:
            print_lose_message