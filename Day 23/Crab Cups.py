from collections import deque

def insert_values(cups, pos, val):

    mid_of_array = len(cups)//2
    ar = []

    if pos <= mid_of_array: #poping lesf
        for ind in range(pos):
            ar.append(cups.popleft())
        # cups.extendleft(val)
        for ind in range(len(val)-1,-1,-1):
            cups.appendleft(val[ind])

        for ind in range(len(ar)):
            cups.appendleft(ar.pop())

    else: #popping right
        for ind in range(pos,len(cups)):
            ar.append(cups.pop())

        cups.extend(val)

        for ind in range(len(ar)):
            cups.append(ar.pop())

    return cups

def play_game(cups, moves):

    cups = deque(cups)

    min_cup = min(cups)
    mac_cup = max(cups)

    for _ in range(moves):

        cur_cup = cups.popleft()
        del_cups= [cups.popleft(), cups.popleft(), cups.popleft()]
        cups.appendleft(cur_cup)

        #find destination
        dest = cur_cup - 1
        if dest < min_cup:
            dest = mac_cup
        while dest in del_cups:
            dest -= 1
            if dest < min_cup:
                dest = mac_cup

        pos = cups.index(dest)+1

        # insert_values(cups, pos, del_cups)

        for item in del_cups:
            cups.insert(pos, item)
            pos += 1

        # tmp = cups[pos-1:]
        # cups = deque(cups[:pos]).extend(del_cups)
        # cups.extend(tmp)


        del_cups = []
        cups.rotate(-1)

    return cups

def count_cups(cups):

    pos = cups.index(1)

    while pos >= 0:
        cups.rotate(-1)
        pos -= 1

    cups.pop()

    return "".join(list(map(str,cups)))

#Part 1

# res = play_game([3,8,9,1,2,5,4,6,7],10)
# res = play_game([4,8,7,9,1,2,3,6,5],100)
# print(res)
#
# res = count_cups(res)
# print(res)

# Part 2

def get_mil_cups(cups, num):

    max_cup = max(cups)+1

    for num in range(max_cup,num):
        cups.append(num)

    return cups

def count_cups2(cups):

    pos = cups.index(1)

    print(cups[pos+1])
    print(cups[pos+2])

    return cups[pos+1] * cups[pos+2]


mil_cups = get_mil_cups([4,8,7,9,1,2,3,6,5], 1000000)
mil_cups = play_game(mil_cups, 10000000)
mil_cups = count_cups2(mil_cups)

print(mil_cups)






