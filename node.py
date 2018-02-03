from random import choice

class Node:

    def __init__(self, x, y):
        # Define the single nodes position
        self.x = x
        self.y = y

        # is node available for movement
        self.available = True

        # Define who it has for neighbors as co-ordinates
        self.neighbors = []

    def addNeighbor(self, neighbor):
        # Adds a neighbor to the node
        self.neighbors.append(neighbor)

    def getRandomNeighbor(self):
        # Get list of available neighbors
        availableNeighbors = []
        for neighbor in self.neighbors:
            if neighbor.available:
                availableNeighbors.append(neighbor)

        # Check the list size and return a random choice
        if len(availableNeighbors) == 0:
            return None
        else:
            return choice(availableNeighbors)

    def makeUnavailable(self):
        self.available = False
