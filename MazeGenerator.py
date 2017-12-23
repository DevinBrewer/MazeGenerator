from PIL import Image

stack = [] # Stack will contain a tuple of x and y
grid_size = 1001 # Make an odd number for clean borders
grid = [[0 for x in range(grid_size)] for y in range(grid_size)] # grid has 0 around outer wall
# Cant touch - 0
# Step - 1
# Untouched - 2
# In stack - 3
x_pos, y_pos = 1, 1


def main():
    # Run the inital setup function
    setup_nodes()

    # Run the generator
    # run_generator()

    # Print the final version of the maze
    print_final()
#
# def run_generator():
#
#     step()
#
#     if len(stack) == 0:
#         return
#
# def step():
#     print(x_pos, y_pos)
#     # Check to see if the "turtle" can can_move
#     if can_move():
#
#
# def can_move():
#     # check in all directions for a 1 somewhere
#     # Up
#     if grid[x_pos][y_pos-2] == 1:
#         print("up")
#         return True
#     # Right
#     if grid[x_pos+2][y_pos] == 1:
#         print("right")
#         return True
#     # Down
#     if grid[x_pos][y_pos+2] == 1:
#         print("Down")
#         return True


def setup_nodes():
    # This will setup the play area
    for i in range(1, grid_size-1, 2):
        for j in range(1, grid_size-1, 2):
            grid[i][j] = 1


def print_final():
    # Prints out the final image, this is called last
    im = Image.new("RGB", (grid_size, grid_size))
    color_grid = []
    for row in grid:
        for cell in row:
            if cell == 0:
                color_grid.append((255, 0, 0))
            elif cell == 1:
                color_grid.append((0, 255, 0))
            else:
                color_grid.append((0, 0, 255))

    im.putdata(color_grid)
    im.show()

def can_move():
    # Returns true or false
    print("test")


if __name__ == '__main__':
    main()
