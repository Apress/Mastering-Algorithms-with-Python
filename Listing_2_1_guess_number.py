def guess_number(lower_bound, upper_bound, num):
    # expand the bounds by 1 to avoid getting stuck in infinite loops
    lower_bound -= 1
    upper_bound += 1
    num_guesses = 1
    guess = (lower_bound + upper_bound) // 2
    print (f"initial guess -->{guess}" )
    while guess != num:
        if guess > num:
            upper_bound = guess
        elif guess < num:
            lower_bound = guess
        else:
            print (f"Guessed it, the number is {guess}")
        guess = (lower_bound + upper_bound) // 2
        print (f"guess -->{guess}" )
        num_guesses += 1
    print (f"it takes {num_guesses} guesses to guess {num}")

if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 100
    num = 99
    guess_number(lower_bound, upper_bound, num)