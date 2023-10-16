import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0
    def roll_die(self, die):
        roll = die.roll()
        if roll == 1:
            self.turn_total = 0
            return 1
        else:
            self.turn_total += roll
            return roll
    def hold(self):
        self.score += self.turn_total
        self.turn_total = 0
    def is_winner(self):
        return self.score >= 100

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = player1
        self.die = Die()
    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]
    def play_turn(self):
        print(f"{self.current_player.name}'s turn:")
        while True:
            decision = input("Enter 'r' to roll or 'h' to hold: ")
            if decision == 'r':
                roll_result = self.current_player.roll_die(self.die)
                print(f"Rolled: {roll_result}")
                print(f"Current Turn Total: {self.current_player.turn_total}")
                if roll_result == 1:
                    print(f"{self.current_player.name} rolled a 1. Turn over.")
                    break
            elif decision == 'h':
                self.current_player.hold()
                print(f"{self.current_player.name} decided to hold.")
                break
    def play_game(self):
        while not self.current_player.is_winner():
            print(f"Current Scores: {self.players[0].name}: {self.players[0].score}, {self.players[1].name}: {self.players[1].score}")
            self.play_turn()
            self.switch_player()

        print(f"{self.current_player.name} wins with a score of {self.current_player.score}!")

if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game(player1, player2)
    game.play_game()
