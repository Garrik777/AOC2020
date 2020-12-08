from pathlib import Path

def read_input(path:str)->list:

    code_lines = []
    index = 0

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')
            code_lines.append(raw_line)

    return code_lines

def get_executed_lines(code_lines:list)->int:

    code_len = len(code_lines)-1
    cur_index = 0
    lowest_index = 0
    line = code_lines[cur_index]
    executed_lines = {}

    while True:

        current_line = line.split(" ")
        action = current_line[0]
        move = int(current_line[1])

        if executed_lines.get(cur_index) != None:
            return executed_lines, False

        executed_lines[cur_index] = current_line

        if cur_index > lowest_index:
            lowest_index = cur_index

        if action == "nop":
            cur_index += 1
        elif action == "acc":
            cur_index += 1
        elif action == "jmp":
            cur_index += move

        if cur_index > code_len:
            return executed_lines, True
        else:
            line = code_lines[cur_index]

    return executed_lines, True

def get_accum(executed_lines:list)->int:

    acc = 0

    for index in executed_lines:

        action = executed_lines[index][0]

        if action == "acc":
            acc += int(executed_lines[index][1])

    return acc

def find_correct_code(executed_lines:list, code_lines:list)->int:

    acc = 0

    for index in executed_lines:

        code_lines_copy = code_lines.copy()
        action = executed_lines[index][0]

        if action == "acc":
            continue

        code_line = code_lines[index]

        if action == "jmp":
            code_line = code_line.replace("jmp","nop")
        elif action == "nop":
            code_line = code_line.replace("nop","jmp")

        code_lines_copy[index] = code_line

        new_executed_lines, without_loop = get_executed_lines(code_lines_copy)

        if without_loop:
            acc = get_accum(new_executed_lines)
            return acc

    return 0

code_lines = read_input("./input.txt")
executed_lines, without_loop = get_executed_lines(code_lines)

acc = get_accum(executed_lines)
print(acc)

acc2 = find_correct_code(executed_lines, code_lines)
print(acc2)



