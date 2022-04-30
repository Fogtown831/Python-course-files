import random
user_action = input("Enter a choice of rock, paper, or scissors: ")
possible_action = ('rock', 'paper', 'scissors')
computer_action = random.choice(possible_action)
print("you chose " + user_action + '. computer chose ' + computer_action)

if user_action == computer_action:
    print("both players selected " + user_action + ". tie")
elif user_action == 'rock':
    if computer_action == 'scissors':
        print('Rock beats scissors. You Win')
    else:
        print('paper beats rock. You lose')

elif user_action == 'scissors':
    if computer_action == 'paper':
        print('scissors beats paper. You Win')
    else:
        print('rock beats scissors. You Lose')

elif user_action == 'paper':
    if computer_action == 'rock':
        print('paper beats rock')
    else:
        print('scissors beats paper. You Lose')