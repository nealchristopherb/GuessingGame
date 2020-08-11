import random
# Generate random number between 1 and 20
secretNum=random.randint(1,20)
# Display secretNum to show that project works correctly.  Would be removed otherwise.
print (secretNum)
# Initialize number of guesses to zero
number_of_guesses= 0 
# User interaction, including input and guess prompt
print ("What is your name?")
userName= input()
# User name prompt using raw_input for v2:
# userName = raw_input("What is your name? ")
print ("Hello, " + userName + ", I have picked a random number between 1 and 20.  Lets see if you can guess it" )
# While loop cycles user guesses and prompts user to try again if their guess is higher or lower than secretNum.
while number_of_guesses <5:
    userGuess=int(input())    
    if secretNum < userGuess:
        if userGuess > 20:
            print ("I said keep it between 1 and 20.   Don't make me come over there!")  
        else: print ("Your guess is too high. Try again." )
#  number_of_guesses is 1ncreased on failed attempts       
        number_of_guesses=number_of_guesses+1
    if secretNum > userGuess:
        if userGuess < 1:
            print ("I said keep it between 1 and 20.  Don't make me come over there!") 
        else: print ("Your guess is too low. Try again")
        number_of_guesses=number_of_guesses+1 
           
# If user guesses correctly:            
    if userGuess==secretNum:
        totalGuesses= str(number_of_guesses +1)
# Separate responses to remain grammatically correct if user guesses correct on one 'try' versus two or more "tries".        
        if number_of_guesses== 0:
               print ("Congratulations! You guessed it in " + totalGuesses + " try!") 
        if number_of_guesses >0:
               print ("Congratulations! You guessed it in " + totalGuesses + " tries!")
# Response if user fails to guess correctly in 5 tries:         
if number_of_guesses >4:
    correctNum= str(secretNum)
    print ("I'm sorry, " + userName + ", but you failed to guess the number in 5 tries.  The correct number was " + correctNum + ".")
