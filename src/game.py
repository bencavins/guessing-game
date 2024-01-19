import random

class Game:
    def __init__(self):
        self.target = random.randint(1, 100)
        self.max_guess_count = 10

    def run(self):
        print('running game')
        # print(f'target == {self.target}')
        guess_count = 0

        while True:
            guess = int(input('Enter a number (between 1-100): '))
            guess_count += 1

            if guess == self.target:
                print('you win!')
                break
            elif guess < self.target:
                print('too low')
            elif guess > self.target:
                print('too high')
            
            if guess_count >= self.max_guess_count:
                print('you lose, too many guesses!')
                break
        
        print(f'You guessed {guess_count} number of times')
        return 