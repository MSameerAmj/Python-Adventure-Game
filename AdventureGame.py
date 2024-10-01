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