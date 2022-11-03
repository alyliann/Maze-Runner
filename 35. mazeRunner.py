#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 19, 2021
#This program completes a maze game code

## This function determines whether or not a given move is legal
def isPositionAvailable(row, col, maze): ## row and col of the place the User wishies to move to
    if row < 0 or col < 0: ## Checks if User is attempting to go out of bounds
        return False
    if maze[row][col] == '1': ## Checks if User is attempting to go thru walls
        return False
    elif maze[row][col] == '0': ## Checks if User is attempting to make legal move
        return True
    else:
        return True

## Given a string representing a maze, this function will place it in a 2d array
def generateMaze(textMaze):
    textMaze = textMaze.split('\n')

    maze = []

    for row in textMaze:
        rowOfMaze = row.split(' ')
        maze.append(rowOfMaze)

    return maze

## Prints out a visual representation of the maze, and where the current user is located
def printMaze(maze, currRow, currCol): ## currRow and currCol represent the Users current location
    rowCount = -1

    for row in maze:
        rowCount += 1
        for stuff in range(3):
            colCount = -1
            for column in row:
                colCount += 1

                ## Location of User
                if rowCount == currRow and colCount == currCol:
                    for i in range(3):
                        print('v', end = '')
                ## Location of wall
                elif column == '1':
                    for i in range(3):
                        print('*', end = '')
                ## Location of hall
                elif column == '0':
                    for i in range(3):
                        print(' ', end = '')
                ## Location of start
                elif column == 'S':
                    for i in range(3):
                        print('S', end = '')
                ## Location of end
                elif column == 'X':
                    for i in range(3):
                        print('X', end = '')
            print()


## This function asks for a string of commands and executes them
def playGame(maze, row, col): ## row and col given here is the starting position
    commands = input("Enter a string of commands: ")

    ## Loops through the given set of commands
    for command in commands:
        ...
        if command == 'R':
            col = col + 1
            if isPositionAvailable(row, col, maze) is False:
                printMaze(maze, row, col)
                print("Cannot move to the Right! Try again :(")
                return False

        if command == 'L':
            col = col - 1
            if isPositionAvailable(row, col, maze) is False:
                printMaze(maze, row, col)
                print("Cannot move to the Left! Try again :(")
                return False

        if command == 'U':
            row = row - 1
            if isPositionAvailable(row, col, maze) is False:
                printMaze(maze, row, col)
                print("Cannot move Up! Try again :(")
                return False

        if command == 'D':
            row = row + 1
            if isPositionAvailable(row, col, maze) is False:
                printMaze(maze, row, col)
                print("Cannot move Down! Try again :(")
                return False

        if (maze[row][col]) == 'X':
            return True

    printMaze(maze, row, col)

    return False

def main():
    print("Hello Everyone! Welcome to Maze Runner!\n\
To succeed in this Computer Science class, you must go through some trials and tribulations...\n\
So tonight, you must pass through our maze!\n\
The game is not over until you have found your path...\n\
And if you try and fail, you must restart from the beginning and try again!\n\
Good luck!")

    ## Reads in a text file containing a maze
    textMazeFile = input("Enter name of text file containing a maze: ")
    textMaze = open(textMazeFile, "r")
    maze = generateMaze(textMaze.read())

    ## The game continues until the User is victorious
    result = False
    while not result:
        print("\nHere is a picture of the maze, provided by some random person down the street ->")
        printMaze(maze, 1, 0)
        result = playGame(maze, 1, 0)

    print("Congrats on escaping the maze! Please do join us again :)")

if __name__ == '__main__':
    main()
