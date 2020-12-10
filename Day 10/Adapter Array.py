from pathlib import Path
from collections import defaultdict

def read_input(path:str)->list:

    numbers = []

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')
            numbers.append(int(raw_line))

    return numbers

def count_differences(jolts:list)->int:


    #we need to add our device jolt
    jolts_copy = jolts.copy()
    jolts_copy.append(jolts[len(jolts)-1] + 3)
    # print(jolts)

    prev_jolt = 0

    one_jolt_diff = 0
    two_jolt_diff = 0
    three_jolt_diff = 0

    for jolt in jolts_copy:

        # print(jolt, prev_jolt)

        diff = jolt - prev_jolt
        prev_jolt = jolt

        if diff == 1:
            one_jolt_diff += 1
        elif diff == 2:
            two_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1

    # print(one_jolt_diff, two_jolt_diff, three_jolt_diff)

    return one_jolt_diff * three_jolt_diff

def count_variations(jolts:list)->int:

    '''
    to count variations we need to determine groups of numbers
    In each group there will be 3 or less possible numbers:
    first group 1-3, second group 2-4, third group 3-5 and so on
    e.g (1,2,3), (2,4), (5), (4,5)

    possible number of variations will be:
    len(group1) * len(group2) * len(group3) and so on
    '''

    groups = []
    current_group = []
    first_num = 1
    last_num = 3
    cur_num = 0
    cur_index = 0

    while cur_num <= last_num and cur_index < len(jolts):

        cur_num = jolts[cur_index]

        if cur_num >= first_num and cur_num <= last_num:
            current_group.append(cur_num)
            cur_index += 1

        else:
            groups.append(current_group)
            min_num = min(current_group)
            max_num = max(current_group)

            new_group = []
            first_num = min_num + 1
            last_num = max_num + 3

            for item in current_group:
                if item >= first_num and item <= last_num:
                    new_group.append(item)

            current_group = new_group


    print(groups)

def count_variations2(jolts:list, first, last, counter)->int:

    current_group = []

    for index in range(len(jolts)-1):

        cur_jolt = jolts[index]

        if cur_jolt >= first and cur_jolt <= last:
            counter += 1
            current_group.append(cur_jolt)
        else:
            min_num = min(current_group) + 1
            max_num = max(current_group) + 3
            count_variations2(jolts[index:], min_num, max_num, counter)

    return counter

def count_variations3(jolts:list):


     first_jolt = jolts[0]

     rest_jolts = jolts[1:]

     second_jolt = rest_jolts[0]

     rest_jolts = jolts[2:]

     third_jolt = rest_jolts[0]

def count_variations4(jolts:list)->int:

    tries = defaultdict(int)
    tries[0] = 1
    for jolt in jolts:

        tries[jolt] = sum([tries[jolt - d] for d in [1, 2, 3]])

    return tries[jolts[-1]]


# jolts = read_input("./test_input.txt")
# jolts = read_input("./test_input2.txt")
jolts = read_input("./input.txt")

jolts.sort()
# print(jolts)
diff = count_differences(jolts)
print(diff)


variations = count_variations4(jolts)
print(variations)



