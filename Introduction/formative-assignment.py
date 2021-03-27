import random

letters = []
score = 0

for num in range (97,123):
    
    letters.append (chr(num))

rlist = random.sample(letters,10)

print('How many words can you make out of the following letters?')
print(*rlist)


# Create a loop that runs until broken by the user.
while True :
    
    guess = input('Try one: ').lower()
    
    invalid = False
    
    # First check length is valid.
    if len(guess) < 3 :
        invalid = True
        print('Invalid answer.. must be more than three letters!')
    # Then check letters are valid.
    else :
        for j in guess :
            if not j in rlist :
                invalid = True
        if invalid :
            print('Invalid answer.. please use the letters provided in the list above!')
    
    # Increment the score for valid answers.
    if not invalid :
        score += 1
    
    # Give user the choice to break the loop.
    if input('Do You Want To Continue? [y/n] ').lower() != 'y':
        break

# Print the final score.
result = 'Final score: ' + str(score)
print(result)

