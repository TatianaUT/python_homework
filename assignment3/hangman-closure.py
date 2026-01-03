# Task 4 Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = " "
        for ch in secret_word:
            if ch in guesses:
                display += ch
            else:
                display += "_"
        print(display)
         # Return True is all letters guessed
        return all(ch in guesses for ch in secret_word)
    return hangman_closure
