import random
# Generate random number between 1 and 20
secretNum=random.randint(1,20)
print (secretNum)
# Initialize number of guesses to zero
number_of_guesses= 0 
# User interaction, including input and guess prompt
print ("What is your name?")
userName= input()
print ("Hello " + userName + " I have picked a random number between 1 and 20.  Lets see if you can guess it" )
# userGuess=int(input())
while number_of_guesses <5:
    userGuess=int(input())    
    if secretNum < userGuess:
        print ("Your guess is too high. Try again." )
        number_of_guesses=number_of_guesses+1
    if secretNum > userGuess:
        print ("Your guess is too low. Try again")
        number_of_guesses=number_of_guesses+1    
    if userGuess==secretNum:
        totalGuesses= str(number_of_guesses +1)
        if number_of_guesses== 0:
               print ("Congratulations! You guessed it in " + totalGuesses + " try") 
        if number_of_guesses >0:
               print ("Congratulations! You guessed it in " + totalGuesses + " tries!")
         
if number_of_guesses >4:
    correctNum= str(secretNum)
    print ("I'm sorry but you failed to guess the number in 5 tries.  The correct number was " + correctNum ".")