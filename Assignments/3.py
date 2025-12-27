#  PART-3
import random, readchar, string
#  Dice roll simulation
count = 0
print('Welcome to the dice game!')
print()
while (count != 10):
    print("Press R to roll die(or Q to quit): ")
    key = readchar.readkey()
    if key.lower() == 'r':
        result = random.randint(1, 6)
        print(result)
        count += 1
    elif key.lower() == 'q':
        print('Goodbye!')
        break
    else:
        print('Wrong key pressed. Try again')
        continue
print('Hope you enjoyed the game. Good day!')
print()

# Coin flip simulation
coin_flip = ["Heads", "Tails"]
head_count = 0
tail_count = 0
print('Coin flip simulation: ')
print()
for count in range(100):
    result = random.choice(coin_flip)
    if result == "Heads":
        head_count += 1
    else:
        tail_count += 1
print(f'Heads: {head_count}')
print(f'Tails: {tail_count}')
print()

#  Lottery Number Generator
print('Lottery numbers:')
print(random.sample(range(1, 50), k=6))
print()

#  PASSWORD GENERATOR
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lower + upper + digits + symbols

password = ''.join(random.choice(all_chars) for i in range(10))

print(f"Generated Password: {password}")
print()

#  GUESS THE NUMBER GAME

print("--- Welcome to the Guessing Game! ---")
print("I'm thinking of a number between 1 and 50.")

secret_number = random.randint(1, 50)
attempts = 0
    
while True:
    try:
        guess = int(input("\nTake a guess: "))
        attempts += 1
        if guess < 1 or guess > 50:
            print("Out of bounds! Please guess between 1 and 50.")
        elif guess < secret_number:
            print("Too LOW! Try again.")
        elif guess > secret_number:
            print("Too HIGH! Try again.")
        else:
            print(f"BINGO! You found it in {attempts} tries.")
            break 
    except ValueError:
        print("Invalid input! Please enter a whole number.")