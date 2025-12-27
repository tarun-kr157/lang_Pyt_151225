import random
#  Rock, paper, scissor game
game = ['rock', 'paper', 'scissors']
while True:
     user = input("\nChoose rock, paper, or scissors: ").lower()
     if user not in game:
         print("Invalid input! Please choose rock, paper, or scissors.")
         continue
     else:
         computer = random.choice(game)
         if user == computer:
             print(f"\nTie! Both players chose {user}")
             break
         elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
             print(f"\nYou win! {user} beats {computer}")
             break
         else:
             print(f"\nComputer wins! {computer} beats {user}")
             break


# Dice game between two players
print("Dice game between two players begins!")
score_A = 0   
score_B = 0
attempts = 5
while (attempts > 0):
    A = random.randint(1, 6)
    score_A += A
    B = random.randint(1, 6)
    score_B += B  
    print(f'\nA got {A}, B got {B}')
    attempts -= 1
if score_A == score_B:
    print(f"\nIt's a tie! A's score: {score_A} = B's score: {score_B}")
elif score_A > score_B:
    print(f"\nA wins! A's score: {score_A} > B's score: {score_B}")
else:
    print(f"\nB wins! A's score: {score_A} < B's score: {score_B}")
print() 