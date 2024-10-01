from enum import Enum
class State(Enum):
    OFF =0
    ON =1 
    

class ItemState(Enum):
    USE =1
    CANNOTUSE =0
    
inventory = []
curr_loc = 'enterance'
map = {
    'enterance' : {
        'toOpen' : None,
        'description' : 'The grand entrance looms with towering stone arches, dim torchlight flickering along cold walls, while a wooden door to the north, guarding the unknown beyond.',
        'items' : [],
        'exits' : {
            'north' : 'courtyard'
            },
        
    },
    'courtyard' : {
        'toOpen' : None,
        'description' : 'The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron_gate. Do not Try to go east!!',
        'items' : ['map', 'torch','iron_gate','key' ],
        'exits' : {
            'west' : 'throne room',
            'north': 'armory',
            'east' : 'fence',
            'South' : 'Enterance',
        },
        
    },
    'throne room': {
        'toOpen': 'torch',
        'description' : 'The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom',
        'items' : ['sword'],
        'exits' : {
            'south' : 'library',
            'north' : 'bedroom',
            'east' : 'courtyard'
        },
        
    },
    'library': {
        'toOpen' : None,
        'description' : 'A room filled with books, with a large wooden desk in the center. To the North, is Throne Room',
        'items' : ['book',],
        'exits': {
            'north' : 'throne room',
        },
        
    },
    'bedroom' : {
        'toOpen': None,
        'description' : 'A cozy bedroom, with a large bed in the center. To the North there is a curtain on a window,seems like something behind curtains.',
        'items' : ['lever','gold_key'],
        'exits' : {
            'south' : 'throne room'
        },
        
    },
    'armory' : {
        'toOpen' : 'iron_gate',
        'description' : 'The armory, lined with rows of glistening swords and battered shields, exudes a metallic scent, with a heavy wooden gate to the north leading to the battlements beyond.',
        'items' : ['shield'],
        'exits' : {
            'south' : 'courtyard',
            'north' : 'exit'
        }        
    },
    'exit': {
        'toOpen' : 'lever',
        'description' : 'WOOHOOO!! You are outside the castle',
        'items' : [],
        'exits' : None
    },
    'fence' : {
        'toOpen': None,
        'description' : 'Game Over! It is a Trap, You fell down into the mountains. ',
        'items' : [],
        'exits' : None
    }
}


Items_in_game = {
    'iron_gate': {
        'status' : ItemState.CANNOTUSE,
        'description' : 'There is a rusty iron_gate.',
        'toUse': 'There must be something very strange to Open the iron_gate.'
    },
    'sword' : {
        'status' : ItemState.USE,
        'description':'There is a shiny sword beside the throne, can be used to fight with enemies.',
        'toUse' : 'There is no enemy ahead'
    },
    'shield' : {
        'status' : ItemState.USE,
        'description':'There is a sheild beside the door, it could protect you from wild animals outside.',
        'toUse' : 'No wild animals inside the castle'
    },
    'key' : {
        'status' : ItemState.USE,
        'description':'There is a key, it could be for something very important.',
        'toUse' : 'There should be something to unlock this feature'
    },
    'book': {
        'status' : ItemState.USE,
        'description': 'There is a book on a large wooden desk.',
        'toUse' : 'Cannot open it! There must be something very strange to see what inside!'
    },
    'lever': {
        'status' : ItemState.CANNOTUSE,
        'description':  'There is a lever on the wall, with a keyhole beside the lever.',
        'toUse' : 'it could be used to open a secret door!'

    },
    'map' : {
        'status' : ItemState.USE,
        'description' : 'There is a map that could lead to some treasure buried in the mountains.',
        'toUse' : 'What there is a riddle on the map, Solve it if you could'
    }, 
    'torch': {
        'status' : ItemState.USE,
        'description': 'There is a torch on the wooden table.',
        'toUse':' There is no light, get some fire or sunlight to see'
    },
    'gold_key':{
        'status' : ItemState.USE,
        'description':'Something is shining, a gold_key.',
        'toUuse': 'you need to have a gadget to open it'
    }
}
hurdles = {
    'iron_gate' : {
        'status' : State.OFF,
        'toOpen' : 'key',
         
    },
    'book' : {
        'status':State.OFF,
        'toOpen':'riddle',
        
              },           
    'lever' :{
        'status':  State.OFF,
        'toOpen': 'gold_key',                
    },
    'torch':{
        'status' : State.OFF,
        'toOpen' : 'torch'
    }
}

def look():
    global curr_loc
    print('==> ', end='')
    print(map[curr_loc]['description'])
    print()
    if map[curr_loc]['items']:
        for item in map[curr_loc]['items']:
            print('==> ', end='')
            print(Items_in_game[item]['description'])
    else:
        print('==> ', end='')
        print(f'No item to explore in {curr_loc}')
    
def take(item):
    global curr_loc
    if item in Items_in_game:
        if Items_in_game[item]['status'] is not ItemState.CANNOTUSE:
            if item not in map[curr_loc]['items'] :
                print('==> ', end='')
                print("Item not in the room! ")
            else:
                inventory.append(item)
                print('==> ', end='')
                print(f'{item} added to inventory')
        else:
            print('==> ', end='')
            print(f'Cannot add {item} in inventory')
    else:
        print('==> ', end='')
        print("Item not in the game!")
    
def solve_riddle(answer):
   for items in hurdles:
        if hurdles[items]['toOpen'] == 'riddle':
            if hurdles[items]['status'] == State.OFF:
                if answer == 'm':
                    print('==> ', end='')
                    print(f'woah ! You solved the riddle, but there is nothing inside the {items}')
                    hurdles[items]['status'] = State.ON  
                else:
                    print('==> ', end='')
                    print('Wrong answer! Try Again')
                    break
            else:
                print('==> ', end='')
                print('riddle already solved')
                break

def check_inventory():
    global inventory
    for item in inventory:
        print(item)
    
    
def drop(item):
    global inventory
    if item in inventory:
        inventory.remove(item)
    else:
        print(f'{item} not in inventory!')
        
def move(direction):
    global curr_loc
    if curr_loc not in map:
        print('==> ', end='')
        print("Error: Invalid location.")
        return    
    if direction not in map[curr_loc]['exits']:
        print('==> ', end='')
        print(f'There is a wall to the {direction} of {curr_loc}. Cannot go ahead!')
        return
    else:
        next_loc = map[curr_loc]['exits'][direction]
        if map[next_loc]['toOpen'] == None or hurdles[map[next_loc]['toOpen']]['status'] == State.ON:
            curr_loc = next_loc
            print('==> ', end='')
            print(f'You moved to {curr_loc}')
            print()
            print('==> ', end='')
            print(map[curr_loc]['description'])
        else:
            print('==> ', end='')
            print(Items_in_game[map[next_loc]['toOpen']]['toUse'])


def use(item):
    if item in Items_in_game:
        if item in inventory:
            if item in map[curr_loc]['items']:
                if item in [items['toOpen'] for items in hurdles.values()]:
                    for items in hurdles:
                        if hurdles[items]['toOpen'] == item:
                            if hurdles[items]['status'] != State.ON:
                                hurdles[items]['status'] = State.ON
                                print('==> ', end='')
                                print(f'{items} opened')    
                            else:
                                return
                else:
                    print('==> ', end='')
                    print(Items_in_game[item]['toUse'])
            else:
                print('==> ', end='')
                print(f'Cannot Use {item} in {curr_loc}')        
        else:
            print('==> ', end='')
            print("Item not in inventory! ")
    else:
        print('==> ', end='')
        print("Invalid Item")

    
def examine(item):
    global  curr_loc
    if item in Items_in_game:
        if item in map[curr_loc]['items']:
            if Items_in_game[item]['status'] == ItemState.CANNOTUSE:
                print('==> ', end='')
                print(Items_in_game[item]['description'], end=" ")
                print(Items_in_game[item]['toUse'])
            else:
                print('==> ', end='')
                print('Cannot examine the item')
        else:
            print('==> ', end='')
            print(f'There is no {item} in {curr_loc}')
    else:
        print('==> ', end='')
        print("Invalid Item")
    
def save(current_location, inventory, hurdles):
        to_save = {
        'current_location': current_location,
        'inventory' : inventory,
        'hurdles_On': hurdles 
        }
        json_object = js.dumps(to_save)
        with open('Saved_Game.json', 'w') as writefile:
            writefile.write(json_object)
    
def Load():
    global curr_loc, inventory
    with open('Saved_game.json' , 'r') as readfile:
        data = js.load(readfile)
        curr_loc = data['current_location']
        inventory = data['inventory']
        hurdle = data['hurdles_On']
        return hurdle
    
## main starts here 

while True:
    print()
    print('---- Gameplay Menu ----')
    print()
    menu = input('==> What would you like to do? ').lower()
    print()
    if(menu == 'quit'):
        print('*****Thanks for playing!*****')
        break
    elif menu == 'play':
        Load_game = input('Do you want to Load previos Game? (Y/N) ').lower()
        if Load_game == 'y':
            alreadysolved_hurdles = Load()
            for hurdle in hurdles:
                if hurdle in alreadysolved_hurdles:
                    hurdles[hurdle]['status'] = State.ON
        print(f'==> You are at {curr_loc}')
        print()
        print(map[curr_loc]['description'])
        print()
        while True:
            command = input('Enter: ').lower()
            command_parts = command.split(' ')
            print()
            if len(command_parts) > 1:
                if 'move' in command:
                    move(command_parts[1])
                elif 'take' in command:
                    take(command_parts[1])
                elif 'use' in command:
                    use(command_parts[1])
                elif 'examine' in command:
                    examine(command_parts[1])
                elif 'drop' in command:
                    drop(command_parts[1])
                else:
                    print('Invalid Syntax')
            else:
                if 'look' in command:
                    look()
                elif command == 'solve riddle':
                    print()
                    print('==> ', end='')
                    riddle = input('Once in a minute, twice in a moment, but never in years. What it is? ').lower()
                    print()
                    solve_riddle(riddle)
                elif command == 'check inventory':
                    check_inventory()
                elif command == 'quit':
                    print()
                    save_game = input('==> Do you want to Save the Game? (Y/N) ').lower()
                    if save_game == 'y':
                        save(curr_loc, inventory, [completed_hurdles for completed_hurdles in hurdles if hurdles[completed_hurdles]['status'] == State.ON])
                        exit(0)
                    else:
                        exit(0)  
                else:
                    print('==> ', end='')
                    print('Invalid command')
            print()
            if curr_loc == 'exit' or curr_loc == 'fence':
                print()
                again = input('==> Do You want to play Again? (Y/N) ').lower()
                print()
                if again == 'y':
                    continue
                else:
                    break
    else:
        print('Invalid Command')