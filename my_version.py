from environment import Environment
from creature import Creature
from plant import Plant

TICK_NB = 30
REFRESH_RATE = .01
MATRIX_SIZE = 2000






if __name__ == "__main__" :
    seb = Creature(speed=15, size=10, x=125, y=125)
    seb2 = Creature(speed=4, size=15, x=10, y=212)
    map = Environment(creatures=[seb])
    # map.get_creatures_stats()

    for i in range(TICK_NB) :
        map.update()
    plt.show()
