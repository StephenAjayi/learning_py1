def create_tunnel (cave_from, cave_to):
    """Create tunnel between cave_from
    and tunnel_to"""
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)

def visit_cave(cave_number):
    """Mark cave as visited"""
    visit_caves.append(cave_number)
    unvisited_caves.remove(cave_number)

def choose_cave(cave_list):
    """Pick a cave from a list, provided
     that the cave has less than 3 tunnels"""
     cave_number = choice(cave_list)
     while len(cave_list[cave_number]) >= 3:
         cave_number = choice(cave_list)
     return cave_number

def print_caves():
    """Print out current cave structure"""
    for number in cave_numbers:
        print number, ":", caves[number]
        print "-----------------"

def setup_caves(cave_numbers):
    """Create the starting list of caves"""
    caves[]
    for cave in cave_numbers:
        caves.append([])
    return caves

def link_caves():
    """Make sure all of the caves are connected
    with two way tunnels"""
    while unvisited_caves != []:
        This_cave = choose_cave(visit_caves)
        next_cave = choose_cave(unvisited_caves)
        create_tunnel(This_cave, next_cave)
        visit_cave(next_cave)

def finish_caves():
    """Link the rest of the caves with one-way tunnels"""
    for cave in cave_numbers:
        while len(this_cave) < 3:
            passage_to = choose_cave(cave_numbers)
            caves[cave].append(passage_to)
