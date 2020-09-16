secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while secret_word != guess and not(out_of_guesses):
    guess_count = guess_count + 1
    if guess_count < guess_limit:
        guess = input('not that one! Try again:')
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print('Sorry! You LOST.')
else:
    print('Viola! you won.')