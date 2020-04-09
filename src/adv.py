from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playerName = input("Please enter your name to begin: ")

player = Player(playerName, room["outside"])

print("Welcome %s!\nYou are currently in the %s room. %s" %
      (player.name, player.current_room.name, player.current_room.description))

direction = ("n", "s", "e", "w")

while True:
    cmd = input(
        "\nPick a direction to move!\n[n] north, [s] south, [e] east, [w] west, [q] quit ~: ")
    try:
        if cmd in direction:
            if getattr(
                    player.current_room, f"{cmd}_to") == None:
                print("There's no room to move to!")
            else:
                player.current_room = getattr(
                    player.current_room, f"{cmd}_to")
                print(
                    f"\nHello {player.name}, you are in {player.current_room.name}. {player.current_room.description}")
        elif cmd == 'q':
            print("Game Over!")
            break
        else:
            print("Please enter a valid command!")
    except ValueError:
        print("This option is not available!")


# 1. Player starts Outside and can only move North (Other Directions return error)
# 2. Player moves North (from Outside) and enters Foyer
# 3. Player can only move South, North, and East (Other directions returns error)
# 4. Player moves South (from Foyer) and goes back to Outside
# 5. PLayer moves North (from Foyer) and enters Overlook
# 6. Player can only move South (from Overlook) and goes back to Foyer
# 7. PLayer moves East (from Foyer) and enters Narrow
# 8. Player can only move West and North (from Narrow) (Other directions return error)
# 9. Player moves West (from Narrow) and goes back to Foyer
# 10. Player moves North (from Narrow) and enters Treasure
# 11. Player can only move South from Treasure back to Narrow
