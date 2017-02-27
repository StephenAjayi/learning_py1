supermarket_list = ['Milk', 'Bread', 'Cheese']

print supermarket_list
print supermarket_list[0]
print supermarket_list[-1]

if 'Milk' in supermarket_list:
    print "Oh good, you remebered the milk!"

wumpus_r_us_list = ['Bow and Arrow', 'Lantern', 'Wumpus B Gone']

print wumpus_r_us_list
print wumpus_r_us_list[0]
print wumpus_r_us_list[-1]

if 'Bow and Arrow' in wumpus_r_us_list:
    print "Oh good, you remembered the bow and arrow!"

wumpus_r_us_list.append('Rope')
wumpus_r_us_list.remove('Wumpus B Gone')

shopping_lists = [supermarket_list, wumpus_r_us_list]

print shopping_lists
