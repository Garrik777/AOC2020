
from pathlib import Path

#Part 1

def read_input(path:str)->list:

    txt_file = Path(path)

    with txt_file.open('r') as f:
        # for line in f.readlines():

        lines = f.readlines()
        bus_lines = lines[1].replace('\n', '')
        bus_lines = bus_lines.split(",")

        timestamp = int(lines[0])
        bus_lines = tuple(int(line) for line in bus_lines if line != "x")

    return timestamp, bus_lines

def fond_closest_time(bus_lines, timestamp):

    min_time = 1000000000
    bus_id = 0

    for bus_line in bus_lines:
        cur_time = (timestamp // bus_line + 1) * bus_line

        if cur_time < min_time:
            min_time = cur_time
            bus_id = bus_line

    return (min_time - timestamp)*bus_id

# timestamp, bus_lines = read_input("./test_input.txt")
# timestamp, bus_lines = read_input("./input.txt")
# print(timestamp)
# print(bus_lines)
# print(fond_closest_time(bus_lines, timestamp))



# Part 2

def read_input2(path:str)->list:

    txt_file = Path(path)

    with txt_file.open('r') as f:
        # for line in f.readlines():

        lines = f.readlines()
        bus_lines = lines[1].split(",")

        #converting bus id's into tuples: (bus id, departue offset)
        bus_lines = tuple(tuple((int(bus_lines[i]),i)) for i in range(len(bus_lines)) if bus_lines[i] != "x")

    return bus_lines


def find_subsequent_departures(bus_lines):

    cur_time = 0
    total_lines = len(bus_lines)
    found = False


    while not found:

        cur_time = cur_time + bus_lines[0][0]
        found = True

        #checking other lines
        for line in range(1,total_lines):

            sub_line = bus_lines[line]
            sub_line_period = sub_line[0]
            sub_line_offset = sub_line[1]

            sub_line_depart = (cur_time // sub_line_period+1)*sub_line_period

            if sub_line_depart != cur_time + sub_line_offset:
                found = False
                break

    return cur_time


# bus_lines = read_input2("./test_input.txt")
# bus_lines = read_input2("./test_input2.txt")
# bus_lines = read_input2("./test_input3.txt")
bus_lines = read_input2("./input.txt")
# print(bus_lines)

subsequent_time = find_subsequent_departures(bus_lines)
print(subsequent_time)
