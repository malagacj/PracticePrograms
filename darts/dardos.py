import random

NUMERO_DE_JUGADORES = 5
NUMERO_DE_RONDAS = 8

class Player:
    def __init__(self, name):
        self.name = name
        self.counter = 121

    def __repr__(self):
        return f'<Player ({self.name})>'


def main():
    print('Bienvenido')

    jugadores = []

    for x in range(1, NUMERO_DE_JUGADORES+1):
        name = input(f'Ingresar jugador el nombre del jugador # {x}: ')
        jugadores.append(Player(name))

    for x in range(1, NUMERO_DE_RONDAS+1):
        print(f'Ronda #{x}')
        for jugador in jugadores:
            jugador.counter -= random.randrange(50)
            print(f'El jugador {jugador.name} obtuvo {jugador.counter} puntos')

    marcador = {}

    for jugador in jugadores:
        if jugador.counter not in marcador:
            marcador[jugador.counter] = []
        marcador[jugador.counter].append(jugador)

    ganadores = marcador[min(marcador)]

    if len(ganadores) == 1:
        print(f'El ganador es {ganadores[0].name}')
    else:
        ganadores_names = [x.name for x in ganadores]
        print(f'Los ganadores son {", ".join(ganadores_names)}')


if __name__ == '__main__':
    main()