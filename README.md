This repository contains functions for managing actions in a text-based adventure game. The game allows players to interact with items in a room, solve riddles, and manage their inventory.

FEATURES
look(): Displays the current room's description and any available items.
take(item): Allows the player to pick up an item and add it to their inventory.
solve_riddle(answer): Provides functionality for solving riddles in the game.
drop(item): Removes an item from the player's inventory.
check_inventory(): Displays the items currently held by the player.

HOW TO USE 
Implement the functions in your game loop and initialize the following game variables:

curr_loc: Tracks the player's current location.
map: Stores game locations and items.
inventory: Stores the player's items.
Items_in_game: Tracks item descriptions and statuses.
hurdles: Manages challenges like riddles.
