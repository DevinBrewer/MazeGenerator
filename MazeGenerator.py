# Import the node and stack class
from stack import Stack
from node import Node

# Import PIL for image procressing
from PIL import Image, ImageDraw
import time

# Make an array of size n of nodes
gridSize = 102 # Always a mutiple of 3
nodeSize = int(gridSize / 3)

# Setup a constant for color white
WHITE = (255, 255, 255)

def main():

    startTime = time.time()

    # Setup the node grid
    nodeGrid = [[Node(x, y) for x in range(nodeSize)] for y in range(nodeSize)]
    setupNodes(nodeGrid)

    # Create the image
    maze = Image.new('RGB', (gridSize, gridSize))
    pixelMap = maze.load()

    # Initiaize the stack
    stack = Stack()
    currentNode = nodeGrid[0][0]
    stack.push(currentNode)

    # Begin the DFS seach
    while not stack.isEmpty():

        # Look at the current node and make it unavailable
        currentNode = stack.getActive()
        currentNode.makeUnavailable()

        # Get the next node
        nextNode = currentNode.getRandomNeighbor()
        if nextNode != None:
            stack.push(nextNode)
            pixelMap = drawLine(pixelMap, currentNode, nextNode)
        else:
            stack.pop()

    # Save the image
    maze.save("Output/maze.png")

    print(time.time() - startTime)

def setupNodes(nodeGrid):
    # Step 1: Tell each node who its neighbors are
    for x in range(nodeSize):
        for y in range(nodeSize):

            currentNode = nodeGrid[x][y]

            # Find the x neighbors
            if x == 0:
                currentNode.addNeighbor(nodeGrid[x+1][y])
            elif x == nodeSize-1:
                currentNode.addNeighbor(nodeGrid[x-1][y])
            else:
                currentNode.addNeighbor(nodeGrid[x-1][y])
                currentNode.addNeighbor(nodeGrid[x+1][y])

            # Find the y neighbors
            if y == 0: # Test the edges before anything else
                currentNode.addNeighbor(nodeGrid[x][y+1])
            elif y == nodeSize-1:
                currentNode.addNeighbor(nodeGrid[x][y-1])
            else:
                currentNode.addNeighbor(nodeGrid[x][y-1])
                currentNode.addNeighbor(nodeGrid[x][y+1])

def drawLine(maze, startNode, endNode):
    # Draw the line on the map
    dx = endNode.x - startNode.x
    dy = endNode.y - startNode.y
    startX = startNode.x * 3 + 1
    startY = startNode.y * 3 + 1
    endX = endNode.x * 3 + 1
    endY = endNode.y * 3 + 1

    maze[startX, startY] = WHITE
    maze[startX + dx, startY + dy] = WHITE
    maze[endX, endY] = WHITE
    maze[endX - dx, endY - dy] = WHITE

    return maze

if __name__ == '__main__':
    main()
