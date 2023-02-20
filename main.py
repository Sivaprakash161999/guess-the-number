### importing the random module
import random

CONTINUE = True

# while this is True, user will be able to restart the game again and again
while CONTINUE:

    print("*************************************")
    print("**** WELCOME TO GUESS THE NUMBER ****")
    print("*************************************")

    lower_bound = False
    while not lower_bound:
        lb = input("Enter the lower bound for the numer range (enter a number within range 1 - 100): ")
        try:
            lb = int(lb)
        except ValueError:
            print("Please enter a valid number")
            continue

        if not (1 <= lb <= 100):
            print("Please enter a number within range 1 - 100(both inclusive)")
            continue
        lower_bound = lb

    upper_bound = False
    while not upper_bound:
        ub = input("Enter the upper bound for the number range (enter a number within range 1000 - 100000): ")
        try:
            ub = int(ub)
        except ValueError:
            print("Please enter a valid number")
            continue

        if not (1000 <= ub <= 100000):
            print("Please enter a number within range 1000 - 100000(both inclusive)")
            continue
        upper_bound = ub

    number_of_turns = False
    while not number_of_turns:
        trn = input("How many turns do you want?(enter a number within range 6 - 20): ")
        try:
            trn = int(trn)
        except ValueError:
            print("Please enter a valid number")
            continue

        if not (6 <= trn <= 20):
            print("Don't be Greedy! Please enter a number within range 6 - 20(both inclusive)")
            continue

        number_of_turns = trn


    random_number = random.randint(lower_bound, upper_bound)


    print("Guess the number between {} and {}".format(lower_bound, upper_bound))
    curr_turn = 1

    while curr_turn <= number_of_turns:

        answer = False
        print("This is turn {}".format(curr_turn))
        while not answer:
            ans = input("Guess the number: ")
            try:
                ans = int(ans)
            except ValueError:
                print("Please enter a valid number")
                continue

            if not (lower_bound <= ans <= upper_bound):
                print("That's not within range. Make a guess between {} and {}, dummy!".format(lower_bound, upper_bound))
                continue
            answer = ans

        ### comparing the guess with the random number
        if answer == random_number:
            print("You have guessed it! GENIUS!!!")
            break
        elif answer < random_number:
            print("That's too low! Try again!")
            curr_turn += 1
        elif answer > random_number:
            print("That's too high! Try again!")
            curr_turn += 1
    else:
        print("You run out of turns!")

    res = ''

    while res not in ['y', 'n']:
        re = input("Do you want to play again?(press 'y' for yes or 'n' for no): ")
        if re not in ['y', 'n']:
            print("That's not a valid option!")
            continue
        res = re

    if re == 'n':
        CONTINUE = False
        print("**************************************")
        print("*** GoodBye! Hope to see you soon! ***")
        print("**************************************")
    else:
        print("****************************")
        print("*** Restarting the game! ***")
        print("****************************")
