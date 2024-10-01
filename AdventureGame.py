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
            
def drop(item):
    global inventory
    if item in inventory:
        inventory.remove(item)
    else:
        print(f'{item} not in inventory!')
        
def check_inventory():
    global inventory
    for item in inventory:
        print(item)