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