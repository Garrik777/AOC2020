
from pathlib import Path
from pprint import pprint

def read_input(path:str)->dict:

    fields = {}
    fields_list = []
    your_ticket = []
    near_tickets = []

    adding_fields = True
    adding_your_ticket = False
    adding_near_tickets = False

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace('\n', '')

            if raw_line == "your ticket:":
                adding_fields = False
                adding_your_ticket = True
                adding_near_tickets = False
                continue
            elif raw_line == "nearby tickets:":
                adding_fields = False
                adding_your_ticket = False
                adding_near_tickets = True
                continue
            elif raw_line == "":
                continue

            if adding_fields:
                cur_field = raw_line.split(":")
                field = cur_field[0].strip()
                values = cur_field[1].split("or")
                fields[field] = []
                for val in values:
                    val_list = val.split("-")
                    start = int(val_list[0].strip())
                    fin = int(val_list[1].strip())
                    fields[field].append((start, fin))
                    fields_list.extend(tuple(i for i in range(int(val_list[0].strip()), int(val_list[1].strip())+1)))

            elif adding_your_ticket:
                your_ticket = tuple(map(int, raw_line.split(",")))
            elif adding_near_tickets:
                near_tickets.append(tuple(map(int, raw_line.split(","))))

    return fields, fields_list, your_ticket, near_tickets

def count_ivalid_values(near_tickets, fields_list)->int:

    invalid_vals = sum([val for ticket in near_tickets for val in ticket if val not in fields_list])
    return invalid_vals

def get_valid_tickets(near_tickets, fields_list)->list:

    valid_tickets = []

    for ticket in near_tickets:

        valid = True
        for val in ticket:
            if val not in fields_list:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    return valid_tickets

def determine_order(valid_tickets, fields, your_ticket)->list:

    '''
    To determine order we take all first numbers in the tickets and search for corresponding class
    Then second, then third, and so on
    '''

    canidates = {}
    unique_fields = []

    ticket_len = len(valid_tickets[0])

    for ind in range(ticket_len):
        cur_values = [ticket[ind] for ticket in valid_tickets]
        cur_values.append(your_ticket[ind])

        canidates[ind] = []

        for key in fields:

            if key in unique_fields:
                continue

            # check = any(item in first_values for item in fields[key])
            # check = all(item in fields[key] for item in cur_values)

            check = True

            first_range = fields[key][0]
            second_range = fields[key][1]

            for val in cur_values:
                if (val < first_range[0] or val > first_range[1]) and (val < second_range[0] or val > second_range[1]):
                    check = False
                    break

            if check:
                canidates[ind].append(key)

        if len(canidates[ind]) == 1:
            unique_fields.append(canidates[ind][0])


    '''
    main problem that there can be multiple fields suitable for ticker ranges
    to solve it we use unique fileds that can be only in one range
    '''

    changed = True

    while changed:
        changed = False

        for ind in range(ticket_len):
            cur_canidate = canidates[ind]

            for u_field in unique_fields:
                if u_field in cur_canidate and len(cur_canidate)>1:
                    cur_canidate.remove(u_field)
                    changed = True

            if len(cur_canidate) == 1:
                unique_fields.extend(cur_canidate)

    return canidates

def get_departue(your_ticket, fields_order)->int:

    multiplier = 1

    for ind in range(len(fields_order)):

        cur_field = fields_order[ind][0]

        if "departure" in cur_field:
            multiplier *= your_ticket[ind]

    return multiplier


# fields, fields_list, your_ticket, near_tickets = read_input("./test_input2.txt")
fields, fields_list, your_ticket, near_tickets = read_input("./input.txt")
# pprint(fields)
# print(fields_list)
# print(your_ticket)
# print(near_tickets)

invalid_val =  count_ivalid_values(near_tickets, fields_list)
print(invalid_val)

valid_tickets = get_valid_tickets(near_tickets, fields_list)
# pprint(valid_tickets)

fields_order = determine_order(valid_tickets, fields, your_ticket)
# pprint(fields_order)

val = get_departue(your_ticket, fields_order)
print(val)