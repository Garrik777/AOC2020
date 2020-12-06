from pathlib import Path
from pprint import pprint


def read_input(path:str)->list:

    groups = []
    group = []

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')

            if len(raw_line) == 0:
                groups.append(group)
                group = []
                continue

            group.append(raw_line)

        groups.append(group)
    return groups

def count_answers(groups:list)->int:

    counter = 0

    for group in groups:
        answers = []
        for person in group:
            for answr in person:
                if answr not in answers:
                    answers.append(answr)
        counter += len(answers)


    return counter

def count_group_answers(groups:list)->int:

    counter = 0

    for group in groups:

        if len(group) == 1:
            counter += len(group[0])
        else:

            answers_in_group = {}

            for person in group:
                for answr in person:
                    if answers_in_group.get(answr) != None:
                        answers_in_group[answr] += 1
                    else:
                        answers_in_group[answr] = 1

            for item in answers_in_group.items():
                if item[1] == len(group):
                    counter += 1

            # pprint(answers_in_group)

    return counter


groups = read_input("./input.txt")
# groups = read_input("./test_input.txt")
# pprint(groups)
pprint(count_answers(groups))
pprint(count_group_answers(groups))


