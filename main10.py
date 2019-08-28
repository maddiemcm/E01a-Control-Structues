#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # prints the statement "Greetings!"
colors = ['red','orange','yellow','green','blue','violet','purple']   # defines colors. this is a list of options to choose from when asked for input
play_again = ''                      # play_again is defined as the input
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):   # while play_again does not equal the character n, and play_again does not equal "no" means that the program will end when the user says n or no but otherwise, play on!
    match_color = random.choice(colors)             #random.choice is a command that chooses a random color from the defined list and match_color is the program that the loop will use: match computers random color choice to the input
    count = 0                                       # count function starts at 0
    color = ''                                      # color equals input
    while (color != match_color):                   # As long as the input color doesn't match the random chosen color, rerun program
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()                  #this allows the computer to not worry about capitalized/lower cased letters, it will see them as the same
        count += 1                                  # This means that each time you guess, it adds one to the original count integral
        if (color == match_color):                  #if input color is equal to random match color then...
            print('Correct!')                       # printed response of "correct" as a result of a correct guess
        else:                                       # What happens if you guess the wrong color
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))     #the printed statement follows an incorrect answer and then tells you how many guesses you have made. Guesses= count is counting the guesses.
    print('\nYou guessed it in {0} tries!'.format(count))     #Tells you how many guesses you've done and formats the integral as the number of guesses
    if (count < best_count):                            # another if then statement. If the number of guesses is less than the max number of guesses the user has already made then...
        print('This was your best guess so far!')       #it prints the statement in quotes
        best_count = count                              #and it logs the new count amount as your new lowest number of guesses
           play_again = input("\nWould you like to play again? ").lower().strip() #Then it promts the user about whether they would like to play again
print('Thanks for playing!')                        #If the user says no, it ends the loop