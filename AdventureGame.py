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
        print("Invalid Item")