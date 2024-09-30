def move(direction):
    global curr_loc
    next_loc = map[curr_loc]['exits'][direction]
    if current_room not in map:
        print("Error: Invalid location.")
        return
    if direction not in map[curr_loc]['exits']:
        print(f'There is a wall to the {direction} of {curr_loc}. Cannot go ahead!')
        return
    else:
        if map[next_loc]['toOpen'] == None or hurdles[map[next_loc]['toOpen']]['status'] == State.ON.value:
            current_room = next_loc
            print(f'You moved to {curr_loc}')
        else:
            print(Items[map[next_loc]['toOpen']]['toUse'])