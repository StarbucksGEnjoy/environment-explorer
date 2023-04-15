from creature import Creature
from plant import Plant

import numpy as np

class Environment():
    '''
        This class corresponds to an environement, containing a map, creatures, plants, who updates itself every tick of the clock.
    '''
    
    def __init__(self, size:int=MATRIX_SIZE, creatures:list=[]) -> None:
        self.matrix:np.array = np.ones((size,size)) # grass
        self.matrix[:size//3, :size//4] = 0  # water
        self.matrix[size-size//6:, :size//3] = 0  # water
        self.creatures:list[Creature] = creatures
        for cre in self.creatures : cre.env = self
        self.create_plants()


    def create_plants(self):
        indices:np.array = np.argwhere(self.matrix == 1)
        nb_plants = int(len(indices)*0.00001)
        self.plants:list[Plant] = []
        for i in range(nb_plants) :
            coordinates = indices[np.random.choice(len(indices))]
            self.plants.append(Plant(x=coordinates[1], y=coordinates[0]))
            # print(self.plants[-1])


    def display(self):
        cmap = plt.cm.colors.ListedColormap(['blue', 'lightgreen', 'green'])
        
        # Plot the matrix with colors
        plt.imshow(self.matrix, cmap=cmap)
        
        for pla in self.plants :
            plt.plot(pla.x, pla.y, marker = '1', markersize=pla.size, color = 'pink')

        for cre in self.creatures :
            plt.plot(cre.y,cre.x, marker='o', markersize=cre.size, color='black')

        plt.draw()
        plt.pause(REFRESH_RATE)
        plt.clf()



    def get_creatures_stats(self):
        for cre in self.creatures :
            print(cre.speed)


    def update(self):
        for cre in self.creatures :
            cre.move()

        self.display()