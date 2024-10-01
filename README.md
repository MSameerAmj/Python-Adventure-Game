Castle Adventure Game
Welcome to the Castle Adventure Game, a text-based adventure where you explore a mysterious castle, solve puzzles, collect items, and navigate through various rooms to achieve your goal. Embark on a thrilling journey filled with challenges and discoveries!

Table of Contents
Introduction
Features
Getting Started
Prerequisites
Installation
Running the Game
Gameplay Instructions
Commands
Game Mechanics
Game Map
Items
Saving and Loading
Contributing
License
Introduction
Castle Adventure Game is a Python-based text adventure that immerses players in an enigmatic castle environment. Navigate through different rooms, interact with various items, overcome hurdles, and solve riddles to progress in the game. Your objective is to explore the castle and find your way out successfully.

Features
Interactive Gameplay: Engage with the game through text commands to move, take items, use items, and more.
Inventory Management: Collect and manage items essential for overcoming obstacles.
Dynamic Map: Explore a detailed map with multiple rooms, each with unique descriptions and challenges.
Puzzles and Riddles: Solve riddles to unlock new areas and advance in the game.
Save and Load Functionality: Save your progress and load previous game states to continue your adventure.
Enum States: Utilize enumerations for managing game states and item usability.

Gameplay Instructions
Upon starting the game, you'll be presented with a gameplay menu. You can choose to start a new game or load a previous one.

Commands
Interact with the game using the following commands:

Movement:

move north
move south
move east
move west
Item Interaction:

take [item] – Pick up an item.
drop [item] – Drop an item from your inventory.
use [item] – Use an item from your inventory.
examine [item] – Get a detailed description of an item.
Game Actions:

look – View the current room's description and available items.
check inventory – View items in your inventory.
solve riddle – Attempt to solve a riddle presented in the game.
quit – Exit the game. You'll be prompted to save your progress.
Game Mechanics
Inventory Management: Collect items to help you navigate and solve puzzles within the castle.
Hurdles: Certain areas or items may be locked and require specific actions or items to overcome.
Riddles: Engage with riddles to unlock new areas or gain special items.
Saving Progress: Save your current game state to continue later.
Game Map
Explore the castle through various interconnected rooms:

Entrance: The grand entrance with stone arches and a wooden door leading north.
Courtyard: Overgrown gardens with a crumbling fountain and exits to the throne room, armory, fence, and back to the entrance.
Throne Room: A majestic room with a stone throne, connected to the library and bedroom.
Library: Filled with books and a large wooden desk.
Bedroom: Cozy room with a large bed and hidden secrets behind curtains.
Armory: Lined with swords and shields, leading to the exit.
Exit: The final destination outside the castle.
Fence: A trap leading to a game over scenario.
Items
Interact with various items to aid your adventure:

Iron Gate: A rusty gate that requires a key to open.
Sword: A shiny weapon for defense.
Shield: Protects against wild animals.
Key: Unlocks important features.
Book: Contains hidden secrets.
Lever: Opens a secret door when used with a gold key.
Map: Reveals treasure locations.
Torch: Provides light in dark areas.
Gold Key: Needed for specific mechanisms.
Saving and Loading
Saving the Game:

Choose to save your game upon quitting.
The game state, including current location, inventory, and hurdles status, is saved to Saved_Game.json.
Loading the Game:

Upon starting the game, choose to load a previous game.
The game will restore your last saved state from Saved_Game.json.
Ensure that Saved_Game.json is in the same directory as the game script.


SAMPLE GAMEPLAY 2:

---- Gameplay Menu ----        

==> What would you like to do? play

Do you want to Load previos Game? (Y/N) n
==> You are at enterance

The grand entrance looms with towering stone arches, dim torchlight flickering along cold walls, while a wooden door to the north, guarding the unknown beyond.

Enter: move north

==> You moved to courtyard

==> The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron_gate. Do not Try to go east!!

Enter: look

==> The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron_gate. Do not Try to go east!!

==> There is a map that could lead to some treasure buried in the mountains.
==> There is a torch on the wooden table.
==> There is a rusty iron_gate.
==> There is a key, it could be for something very important.

Enter: take key

==> key added to inventory

Enter: take torch

==> torch added to inventory

Enter: take map

==> map added to inventory

Enter: move west

==>  There is no light, get some fire or sunlight to see

Enter: use torch

==> torch opened

Enter: move west

==> You moved to throne room

==> The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom

Enter: move south

==> You moved to library

==> A room filled with books, with a large wooden desk in the center. To the North, is Throne Room

Enter: look

==> A room filled with books, with a large wooden desk in the center. To the North, is Throne Room

==> There is a book on a large wooden desk.

Enter: take book

==> book added to inventory

Enter: use book

==> Cannot open it! There must be something very strange to see what inside!

Enter: move north

==> You moved to throne room

==> The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom

Enter: move east

==> You moved to courtyard

==> The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron_gate. Do not Try to go east!!

Enter: use map

==> What there is a riddle on the map, Solve it if you could

Enter: solve


==> Once in a minute, twice in a moment, but never in years. What it is? m

==> woah ! You solved the riddle, but there is nothing inside the book

Enter: move west

==> You moved to throne room

==> The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom

Enter: move north

==> You moved to bedroom

==> A cozy bedroom, with a large bed in the center. To the North there is a curtain on a window,seems like something behind curtains.
Enter: look

==> A cozy bedroom, with a large bed in the center. To the North there is a curtain on a window,seems like something behind curtains.
==> There is a lever on the wall, with a keyhole beside the lever.
==> Something is shining, a gold_key.

Enter: take gold_key

==> gold_key added to inventory

Enter: take lever

==> Cannot add lever in inventory

Enter: use lever

==> Item not in inventory!

Enter: use gold_key

==> lever opened

Enter: move south

==> You moved to throne room

==> The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom

Enter: move east

==> You moved to courtyard

==> The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron_gate. Do not Try to go east!!

Enter: use key

==> iron_gate opened

Enter: move south

==> There is a wall to the south of courtyard. Cannot go ahead!

Enter: move north

==> You moved to armory

==> The armory, lined with rows of glistening swords and battered shields, exudes a metallic scent, with a heavy wooden gate to the north leading to the battlements beyond.

Enter: move north

==> You moved to exit

==> WOOHOOO!! You are outside the castle


==> Do You want to play Again? (Y/N) y


SAMPLE GAMEPLAY 2
