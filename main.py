import random
import art
import words

chosen_word = random.choice(words.word_list)

print(art.logo)

lives = 6

display = []
for i in range(len(chosen_word)):
    display.append('_')
print(display)

end = False

while not end:

    guess = input("Guess a letter: ").lower()

    for position in range(0,len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'You guess {guess}, that is not in the word. You lose a life')
        lives -= 1
        if lives == 0:
            end = True
            print("You lose :(")

    print(f"{' '.join(display)}")

    if '_' not in display:
        end = True
        print("You Win!!")

    print(art.stages[lives])

print(f'The word was {chosen_word}')