from enum import Enum
class State(Enum):
    ON =1 
    OFF =0

class ItemState(Enum):
    USE =1
    CANNOTUSE =0

map = {
    'Enterance' : {
        'status' : State.ON,
        'description' : 'The grand entrance looms with towering stone arches, dim torchlight flickering along cold walls, while a wooden door to the north, guarding the unknown beyond.',
        'items' : None,
        'exits' : {
            'north' : 'CourtYard'
            },
        'itemsToUse' : None
    },
    'CourtYard' : {
        'STATUS': State.ON,
        'description' : 'The courtyard, ringed by stone walls and overgrown gardens, holds a crumbling fountain, with red velvet curtains to the west leading further into the castle.To the North there is a heavy rusty iron gate. Do not Try to go east!!',
        'items' : ['map', 'torch', ],
        'exits' : {
            'west' : 'Throne room',
            'North': 'Armory',
            'East' : 'Fence',
            'South' : 'Enterance',
        },
        'itemsToUse' : {
            'key' : State.ON
        }
    },
    'Throne Room': {
        'status' : State.OFF,
        'description' : 'The grand throne room, with a large stone throne at the far end, To the South you can see some books through a slightly opened door. North goes to a bedroom',
        'items' : ['Sword'],
        'exits' : {
            'south' : 'Library',
            'north' : 'Bedroom',
            'east' : 'CourtYard'
        },
        'itemsToUse' : {
            'Torch' : State.ON
        }
    },
    'Library': {
        'status' : State.ON,
        'description' : 'A room filled with books, with a large wooden desk in the center. To the North, is Throne Room',
        'items' : ['Book'],
        'exits': {
            'North' : 'Throne Room',
        },
        'itemsToUse' : {
            'map' : State.ON
        }
    },
    'Bedroom' : {
        'status' : State.ON,
        'description' : 'A cozy bedroom, with a large bed in the center. To the North there is a curtain on a window,seems like something behind curtains.',
        'items' : ['Lever'],
        'exits' : {
            'south' : 'Throne Room'
        },
        'itemsToUse' : {
            'Lever' : State.ON
        }
    },
    'Armory' : {
        'status' : State.OFF,
        'description' : 'The armory, lined with rows of glistening swords and battered shields, exudes a metallic scent, with a heavy wooden gate to the north leading to the battlements beyond.',
        'items' : ['Shield'],
        'exits' : {
            'south' : 'Courtyard',
            'North' : 'exit'
        }
    },
    'exit': {
        'status' : State.ON,
        'description' : 'WOOHOOO!! You are outside the castle',
        'items' : None,
        'exits' : None
    },
    'Fence' : {
        'status' : State.ON,
        'description' : 'Game Over! It is a Trap, You fell down into the mountains. ',
        'items' : None,
        'exits' : None
    } 
}

Items : {
    'Sword' : {
        'status': State.ON,
        'description':'There is a shiny sword beside the throne, can be used to fight with enemies',
    },
    'sheild' : {
        'status' : State.ON,
        'description':'There is a sheild beside the door, it could protect you from wild animals outside'
    },
    'key' : {
        'status' : State.ON,
        'description':'There is a key, it could be for something very important',
    },
    'book': {
        'status' : State.OFF,
        'description': 'There is a book on a large wooden desk. You need to solve the riddle to open it'
    },
    'lever': {
        'status' : State.OFF,
        'description':  'There is a lever on the wall, it could be used to open the secret door, There is a keyhole beside the lever',
    },
    'map' : {
        'status' : State.ON,
        'description' : 'Map of an old treasure buried somewhere in the mountains'
    },
    
}