
from pathlib import Path
from pprint import pprint

class Bag():
    def __init__(self, bag_name, contains=None):
        self.bag_name = bag_name
        self.contains = contains

    def __repr__(self):
        return f"{self.bag_name}:{self.contains}"

def read_input(path:str)->dict:

    txt_file = Path(path)
    created_nodes = {}

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('.\n', '')
            raw_line = raw_line.replace('bags.', '')
            raw_line = raw_line.replace('bags', '')
            raw_line = raw_line.replace('bag', '')

            bags = list(map(lambda line: line.strip(), raw_line.split("contain")))

            # pprint(bags)

            if len(bags) == 2:
                parent_bag = bags[0]
                child_bag = bags[1]

                if created_nodes.get(parent_bag) == None:
                    created_nodes[parent_bag] = Bag(parent_bag)

                # lowest level
                if child_bag == "no other":
                    continue
                else:
                    # print(parent_bag)
                    # print(child_bag)
                    child_bags = list(map(lambda line: line.strip(), child_bag.split(",")))

                    contains = []

                    for bag in child_bags:

                        quantity = int(bag[0])
                        name = bag[1:].strip()
                        # print(quantity)
                        # print(name)

                        if created_nodes.get(name) == None:
                            created_nodes[name] = Bag(name)

                        contains.append([created_nodes[name], quantity])

                    created_nodes[parent_bag].contains = contains

    return created_nodes

def check_my_bag(bags, my_bag_name):

    counter = 0

    for bag in bags.items():
        child_bag = bag[1]

        if child_bag.contains == None:
            continue

        string = str(child_bag.contains)

        if my_bag_name in string:
            counter += 1

    return counter

def count_nested_bags(array):

    counter = 0

    if array == None:
        return 0

    for bag in array:
        # pprint(bag[0])
        # pprint(bag[1])

        cur_bag = bag[0]
        counter += bag[1]
        multiplier = bag[1]

        if cur_bag.contains != None:
            counter += multiplier * count_nested_bags(cur_bag.contains)

    return counter

def find_nested_bags(bags, my_bag_name):

    my_bag = bags[my_bag_name]
    counter = count_nested_bags(my_bag.contains)
    return counter


my_bag = "shiny gold"
#bags = read_input("./test_input.txt")
bags = read_input("./input.txt")
# pprint(bags)

counts = check_my_bag(bags, my_bag)
print(counts)

nested_bags = find_nested_bags(bags, my_bag)
print(nested_bags)







