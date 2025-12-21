import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📃' }
choices = ('r', 'p', 's')

while True:

    user_choice = input('Rock, paper, or scissors? (r/p/s)').lower()
    if user_choice != 'r' and user_choice != 'p' and user_choice != 's':
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
     ((user_choice == 'r'and computer_choice == 's') or
     (user_choice == 's' and computer_choice == 'p') or
     (user_choice == 'p' and computer_choice == 'r'))
         print('You win!')
    else:
        print(' Too bad You lose!')

    should_continue = input('Countinue? (y/n).lower()')
    if should_continue == 'y':
        break

