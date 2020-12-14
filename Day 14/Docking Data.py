from pathlib import Path
from itertools import product

# Part 1

def get_adress_value(code_line:str)->int:

    code_lines = code_line.split("=")

    mem_adress = code_lines[0].strip()
    mem_adress = mem_adress[4:]
    mem_adress = int(mem_adress[:mem_adress.find("]")])

    value = int(code_lines[1].strip())

    return mem_adress, value

def apply_mask(number, mask)->int:

    # print(mask)

    b_number = f"{number:036b}"
    b_number = [char for char in b_number]
    # print(b_number)
    # print([char for char in mask])

    for ind in range(36):
        if mask[ind] == "X":
            continue
        b_number[ind] = mask[ind]

    # print(b_number)
    new_number = "".join(b_number)
    # print(new_number)
    new_number = int(new_number, 2)
    # print("-------------------------------")

    return new_number

def read_input(path:str)->dict:

    mem = {}

    txt_file = Path(path)

    with txt_file.open('r') as f:

        current_mask = ""

        for line in  f.readlines():

            raw_line = line.replace('\n', '')

            if raw_line[:3] == "mem":
                # print(raw_line)
                mem_adrees, value = get_adress_value(raw_line)
                # print(mem_adrees, value)
                mem[mem_adrees] = apply_mask(value, current_mask)


            else:
                current_mask = raw_line.split("=")
                current_mask = current_mask[1].strip()
                # print(current_mask)

    return mem

mem = read_input("./input.txt")
print(sum(mem.values()))

# Part 2

def apply_mask2(number, mask)->int:

    b_number = f"{number:036b}"
    b_number = [char for char in b_number]

    for ind in range(36):
        if mask[ind] == "0":
            continue
        b_number[ind] = mask[ind]

    return b_number

def get_mem_adress(masked_mem_adress):

    x_indicies = [ind for ind, item in enumerate(masked_mem_adress) if item == 'X']
    x_ind_len = len(x_indicies)

    for res in product([0,1], repeat=x_ind_len):
        for ind in range(x_ind_len):
            masked_mem_adress[x_indicies[ind]] = str(res[ind])
        yield "".join(masked_mem_adress)

def  wright_value_to_memory(masked_mem_adress, value, mem):

    for mem_adress in get_mem_adress(masked_mem_adress):

        mem[mem_adress] = value

def read_input2(path:str)->dict:

    mem = {}

    txt_file = Path(path)

    with txt_file.open('r') as f:

        current_mask = ""

        for line in  f.readlines():

            raw_line = line.replace('\n', '')

            if raw_line[:3] == "mem":
                mem_adress, value = get_adress_value(raw_line)
                masked_mem_adress = apply_mask2(mem_adress, current_mask)

                wright_value_to_memory(masked_mem_adress, value, mem)

            else:
                current_mask = raw_line.split("=")
                current_mask = current_mask[1].strip()

    return mem

mem = read_input2("./input.txt")
print(sum(mem.values()))


