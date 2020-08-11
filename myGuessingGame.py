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
        print ("Your guess is too high. Try again")
        number_of_guesses=number_of_guesses+1
    if secretNum > userGuess:
        print ("Your guess is too low. Try again")
        number_of_guesses=number_of_guesses+1    
    if userGuess==secretNum:
        print("Congratulations! You got it!")
        break   
        