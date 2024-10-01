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

