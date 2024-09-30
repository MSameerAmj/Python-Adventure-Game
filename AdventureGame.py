def look ():
    global curr_loc
    print(map[curr_loc]['description'])
    for item in map[curr_loc]['items']:
        print(Items_in_game[item]['description'])

def take(item):
    global curr_loc
    if item in map[curr_loc]['items'] :
        inventory.append(item)
        print(f'{item} added to inventory')
    else:
        print("Item not in the room! ")    