# Homework Assignment: myGuessingGame.py
![]/1_Km98PgzRp9yRYfVZeSzwzQ.png
## Goal: 
    To create a guessing game using Python that generates a random number and invites the user to try and guess it.

## Details/Requirements:

**_First,_** the game will ask for the user's name and this will be a collected string an printed to the screen

**_Given_** that the user guesses a number starts the guessing game with a random number
    
**_When_** the user guesses a number the computer will give various hints if the number is too high or too low
    
**_Then_** when user guesses the correct number the computer will print the answer along with the number of attempts by the user    

## Execution:
Was able to get a working version for Python v3 and v2.  The v2 version is commented out in the submitted file.  

As prescribed, the file use the **random** module and random.randint to generate a random number between 1 and 20

File uses a while loop to cycle through 5 guesses (launching from 0, incrementing by 1 on each incorrect guess and stopping if 'number_of_guesses' variable reaches 4).  With the 4 loop there are **if** statements that alert user that their choice is too high or too low.  

I also added lines of code to display the code for verification of the product, to make sure that the user's choice fit between the choice parameters (1-20)

Next the file tracks the number of guesses by the user and reports them to the user if the user guesses correctly.  Code was added here to maintain correct languauge: 

    Congratulations! You guessed it in 1 try!"
        
        instead of

    "Congratulations! You guessed it in 1 tries!"

Lastly, if the user fail to guess correctly and the number_of_guesses variable reaches 4, gameplay ends and the number is revealed.      
