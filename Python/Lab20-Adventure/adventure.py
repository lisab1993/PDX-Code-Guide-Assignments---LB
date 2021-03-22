#===================================================
#   MODIFICATIONS
# use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)
#use different unicode characters (you can find lists online)
#add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side
#add an inventory system
#===================================================
#   CLASSES
class Creature:
    '''all heroes and enemies will have location coordinates, a symbol, and health meter'''
    def __init__(self, location_i, location_j, character, health):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character
        self.health = health

# player class (which inherits from creature)
# which defaults to having a smiley face as the character and 10 for the health
class Player(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⚔', 10) # invoking the parent class's initializer

class Item(Creature):

    def __init__(self, location_i, location_j)
     super().__init__(location_i, location_j, 🟔, 1)   


# enemy class (which inherits from creature)
# which defaults to having a squiggley as the character and 4 for the health
class Enemy(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☠', 4) # invoking the parent class's initializer
    

# board class which represents the board
class Board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.grid = [] # list of lists of strings
        self.creatures = []

        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(' ')
            self.grid.append(row)
    
    def add_creature(self, creature):
        self.creatures.append(creature)

    def print_board(self):
        print('  j ', end='')
        for j in range(self.width):
            print(j, end=' ')
        print()
        print('i  ' + '-'*self.width*2)
        # loop over the rows
        for i in range(self.height):
            print(str(i) + ' |', end=' ')
            # loop over the columns
            for j in range(self.width):
                # find out if there's a creature at the given location
                # if there is, print out its character
                # if there isn't, print out a space
                for creature in self.creatures:
                    if i == creature.location_i and j == creature.location_j:
                        print(creature.character, end=' ')
                        break
                else:
                    print(self.grid[i][j], end=' ')  # otherwise print the board square
            print('|')
        print('   ' + '-'*self.width*2)




    

#______________________________________________________________________
#   SPECIFICATIONS OF BOARD AND CHARACTERS
board = Board(10, 10)

player = Player(2, 2)
board.add_creature(player)

enemy1 = Enemy(5, 6)
board.add_creature(enemy1)

enemy2 = Enemy(1, 3)
board.add_creature(enemy2)

enemy3 = Enemy(0, 0)
board.add_creature(enemy3)

item1 = 

enemies = [enemy1, enemy2, enemy3]
#_____________________________________________________________________
#   REPL
opening_story = "You are locked in a dungeon with strange monsters. Find the way out and don't die. Pretty easy right? Don't forget: Do. Not. Die. That is literally your only goal. Don't mess that up."
print(opening_story)
print("")

inventory = {#blank dictionary where items will be the key, and their description will be the value.
"health pack":"Increases health by 5 points. Too bad this one is empty and you can't use it yet.",
"pen":"The pen is mightier than the sword, my friend. It also stains the best shirts of your enemies.",
} 


while True:
    board.print_board()
    # use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)
    command = input('what is your command? ').lower().strip()  # get the command from the user

    if command == 'done':
        break  # exit the game

    elif command in ["left", "l","west", "w"]:# LEFT MOVEMENT
        if player.location_j != 0:#check if the player is at the left wall
            player.location_j -= 1  # move left if we're not at the wall
        else:# if the player is at the left wall, they will appear at the other side.
            player.location_j = board.width - 1# the end will always be the width of the board -1 (to account for the zero in the list index)

    elif command in ["right", "r", "east", "e"]:# RIGHT MOVEMENT
        if player.location_j != board.width - 1:
            player.location_j += 1  # move right
        else:
            player.location_j = 0

    elif command in ["up", "u", "north", "n"]:# UP MOVEMENT
        if player.location_i != 0:# move up
             player.location_i -= 1
        else:
            player.location_i = board.height - 1 

    elif command in ["down", "d", "south", "s"]:# DOWN MOVEMENT
        if player.location_i != board.height - 1:   # move down
            player.location_i += 1
        else:
            player.location_i = 0

    elif command == "inventory":
        print(inventory)

    # does the player overlap with any enemy?
    for enemy in enemies:
        if player.location_i == enemy.location_i and player.location_j == enemy.location_j:
            print('You encountered an enemy!')
    
