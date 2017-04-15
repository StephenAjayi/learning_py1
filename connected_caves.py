from random import choice

# setup caves

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves != []:
    i = choice(visited_caves)
    print len(caves[i])
    if len(caves[i]) >= 3:
        continue

    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)

    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)

    for number in cave_numbers:
        print number, ":", caves[number]
    print '____________'

for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = choice(cave_numbers)
        # if len(caves[passage_to]) >= 3:
        #     continue
        # if passage_to == i:
        #     random_cave = choice(caves)
        #     random_tunnel_choice = choice(range(0,2))

        caves[i].append(passage_to)
        # caves[passage_to].append(i)
        for number in cave_numbers:
            print number, ":", caves[number]
        print '____________'
