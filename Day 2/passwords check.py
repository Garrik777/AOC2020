
from pathlib import Path
import collections

def read_input(path:str)->list:

    txt_file = Path(path)
    if not txt_file.is_file():
        return []

    ls = []

    with txt_file.open('r') as f:
        for password in f.readlines():

            pwd_settings = password.split(" ")
            passwords = {}
            passwords["symb_num"] = pwd_settings[0]
            passwords["symb"] = pwd_settings[1][0]
            passwords["pwd"] = pwd_settings[2].replace('\n', '')

            ls.append(passwords)
    return ls

def check_pwd_counter(pwd:str, symb:str, range:str)->int:
    count = collections.Counter(pwd)
    rng = range.split("-")
    first = int(rng[0])
    last = int(rng[1])

    if count.get(symb) != None:
        counts = count[symb]

        if first <= counts and counts <= last:
            return 1
        else:
            return 0
    else:
        return 0

def char_counter(pwd:str)->dict:
    counter = {}
    for char in pwd:
        if counter.get(char) != None:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter

def check_pwd(pwd:str, symb:str, range:str)->int:
    count = char_counter(pwd)
    rng = range.split("-")
    first = int(rng[0])
    last = int(rng[1])

    if count.get(symb) != None:
        counts = count[symb]

        if first <= counts and counts <= last:
            return 1
        else:
            return 0
    else:
        return 0

def check_pwd_problem2(pwd:str, symb:str, range:str)->int:

    rng = range.split("-")
    first = int(rng[0])
    last = int(rng[1])

    first_letter = pwd[first-1]
    last_letter = pwd[last-1]

    if first_letter == symb and last_letter == symb:
        return 0
    elif first_letter == symb:
        return 1
    elif last_letter == symb:
        return 1
    else:
        return 0


input = read_input("./input.txt")

valid_count = 0
for line in input:
    valid_count += check_pwd_counter(line["pwd"], line["symb"], line["symb_num"])

print(valid_count)

valid_count = 0
for line in input:
    valid_count += check_pwd(line["pwd"], line["symb"], line["symb_num"])

print(valid_count)

valid_count = 0
for line in input:
    valid_count += check_pwd_problem2(line["pwd"], line["symb"], line["symb_num"])

print(valid_count)












