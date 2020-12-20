from pathlib import Path

def read_input(path:str)->dict:

    rules = {}
    messages = []

    readingRules = True
    readingMessages = False

    txt_file = Path(path)
    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace("\n","").strip()

            if raw_line == "":
                readingRules = False
                readingMessages = True
                continue

            if readingRules:
                rule = raw_line.split(":")
                rule_number = int(rule[0])

                if "|" in rule[1]:
                    sub_split = rule[1].strip().split("|")
                    sub_list = []

                    for item in sub_split:
                        sub_list.append(list(map(int,item.strip().split(" "))))

                    rules[rule_number] = sub_list

                else:

                    simple_rule = rule[1].replace('"','').strip()
                    if simple_rule.isalpha():
                        rules[rule_number] = simple_rule
                    else:
                        rules[rule_number] = [list(map(int,simple_rule.split(" ")))]

            elif readingMessages:
                messages.append(raw_line.strip())

    return rules, messages

def combine_rules(rules):

    somethinChanged = True

    while somethinChanged:

        somethinChanged = False

        for rule in rules:

            current_rule = rules[rule]

            for ind in range(len(current_rule)):

                cur_item = current_rule[ind]

                if isinstance(cur_item, int):
                    sub_rule = rules[cur_item]

                    if isinstance(sub_rule, str):
                        current_rule[ind] = sub_rule
                        somethinChanged = True
                    elif isinstance(sub_rule, list) and isinstance(sub_rule[0][0], str):
                        current_rule[ind] = sub_rule

                elif isinstance(cur_item, list):

                    cur_1 = cur_item[0]
                    cur_2 = cur_item[1]

                    if isinstance(cur_1, str) or isinstance(cur_2, str):
                        continue

                    sub_rule1 = rules[cur_item[0]]
                    sub_rule2 = rules[cur_item[1]]

                    if isinstance(sub_rule1, str) and isinstance(sub_rule2, str):
                        current_rule[ind] = sub_rule1 + sub_rule2
                        somethinChanged = True
                    elif isinstance(sub_rule1, list) and isinstance(sub_rule2, list):
                        subsubrule11 = sub_rule1[0]
                        subsubrule12 = sub_rule1[1]
                        subsubrule21 = sub_rule2[0]
                        subsubrule22 = sub_rule2[1]

                        if isinstance(subsubrule11,str):
                            current_rule[ind] = [subsubrule11+subsubrule21, subsubrule11+subsubrule22,
                                                 subsubrule12+subsubrule21, subsubrule12+subsubrule22]

                        somethinChanged = True




    return rules

def check(msg, rule):
    if type(rules[rule]) == str:
        if msg and msg[0] == rules[rule]:
            return [msg[1:]]
    else:
        a = []
        for b in rules[rule]:
            zm = [msg]
            for r in b:
                zm2 = []
                for x in zm:
                    zm2 += check(x, r)
                zm = zm2
                if not zm:
                    break
            if zm:
                a += zm
        return a
    return []

# rules, messages = read_input("./test_iput.txt")
rules, messages = read_input("./input.txt")
print(rules)

print(sum('' in check(msg, 0) for msg in messages))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

print(sum('' in check(msg, 0) for msg in messages))


# rules = combine_rules(rules)
# print(rules)
#
# rule0 = ""
#
# # for item in rules:
# #     if len(item)