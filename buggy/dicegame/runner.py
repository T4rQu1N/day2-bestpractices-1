from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.reroll()
        self.reset()

    def reroll(self):
        self.dice = Die.create_dice(5)

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        
        total = 0
        for die in self.dice:
            total += die.value
            #print(Die.roll(self))
        #print(total)
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        roundCounter = 1

        while True:
            runner = cls()
            

            print("Round {}\n".format(roundCounter))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
                
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            roundCounter += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[y/n]: ")

            if prompt == 'y':
                runner.reroll()
            elif prompt == 'n':
                i_just_throw_an_exception()
                runner.reset()
                pass
