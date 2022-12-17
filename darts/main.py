import random

NUM_PLAYERS = 3
NUM_ROUNDS = 3

class Player:
    def __init__(self, name):
        self.name = name
        self.counter = 121

    def __repr__(self):
        return f'<Player ({self.name})>'

    def play(self):
        self.counter -= random.randrange(50)

    def get_counter_verbose(self):
        return f'El jugador {self.name} obtuvo {self.counter} puntos'


class Game:
    def __init__(self, num_players, num_rounds):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.players = []
        self.final_score = {}

    def initialize_players(self):
        for x in range(self.num_players):
            name = input(f'Ingresar el nombre del jugador # {x+1}: ')
            self.players.append(Player(name))

    def set_final_score(self):
        for player in self.players:
            if player.counter not in self.final_score:
                self.final_score[player.counter] = []
            self.final_score[player.counter].append(player)

    def execute_rounds(self):
        for x in range(self.num_rounds):
            print(f'Ronda #{x+1}')
            for player in self.players:
                player.play()
                print(player.get_counter_verbose())
        self.set_final_score()

    def get_winners(self):
        return self.final_score[min(self.final_score)]

    def show_winners(self):
        winners = self.get_winners()
        if len(winners) == 1:
            print(f'El ganador es {winners[0].name}')
        else:
            winners_names = [x.name for x in winners]
            print(f'Los ganadores son {", ".join(winners_names)}')

    def start(self):
        print('Bienvenido')
        self.initialize_players()
        self.execute_rounds()
        self.show_winners()


if __name__ == '__main__':
    game = Game(NUM_PLAYERS, NUM_ROUNDS)
    game.start()
