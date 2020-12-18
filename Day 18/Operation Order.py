
from pathlib import Path
import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Part 1

def calculate(eval_expr):

    #"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

    exp_list = eval_expr.split(" ")

    if len(exp_list) == 3:
        op = operatorlookup.get(exp_list[1])
        res = op(int(exp_list[0]), int(exp_list[2]))
        return res

    res = int(exp_list[0])

    for ind in range(1, len(exp_list),2):
        op = operatorlookup.get(exp_list[ind])
        res = op(res, int(exp_list[ind+1]))
    return res

def eval_expression(expression):

    stack = []

    for char in expression:

        if char == ")":
            cur_char = char
            cur_expr = []
            while cur_char != "(":
                cur_char = stack.pop()
                cur_expr.append(cur_char) #values returned in reverse order so we will need to revrse them back

            cur_expr.pop() #last elem is "(". we need to remove it
            eval_expr = ""
            for _ in range(len(cur_expr)):
                eval_expr += cur_expr.pop()

            res = calculate(eval_expr)
            stack.append(str(res))


        else:
            stack.append(char)

    eval_expr = ""
    for val in stack:
        eval_expr += val

    return calculate(eval_expr)

def read_input(path:str)->dict:

    sum = 0

    txt_file = Path(path)
    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace("\n","")

            sum += eval_expression(raw_line)

    return sum

# res = eval_expression(expression)
# print(res)

res = read_input("./input.txt")
print(res)

# Part 2

def calculate2(eval_expr):

    #addition is evaluated before multiplication
    #"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    # "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    #"2 * 3 + 20"

    stack = []
    exp_list = eval_expr.split(" ")

    if len(exp_list) == 3:
        op = operatorlookup.get(exp_list[1])
        res = op(int(exp_list[0]), int(exp_list[2]))
        return res

    pass_iter = False
    for ind in range(len(exp_list)):

        if exp_list[ind] == "+" or exp_list[ind] == "-":
            op = operatorlookup.get(exp_list[ind])
            prev_val = stack.pop()
            res = op(int(prev_val), int(exp_list[ind+1]))
            stack.append(str(res))
            pass_iter = True
        else:
            if not pass_iter:
                stack.append(exp_list[ind])
            pass_iter = False

    return calculate(" ".join(stack))

def eval_expression2(expression):

    stack = []

    for char in expression:

        if char == ")":
            cur_char = char
            cur_expr = []
            while cur_char != "(":
                cur_char = stack.pop()
                cur_expr.append(cur_char) #values returned in reverse order so we will need to revrse them back

            cur_expr.pop() #last elem is "(". we need to remove it
            eval_expr = ""
            for _ in range(len(cur_expr)):
                eval_expr += cur_expr.pop()

            res = calculate2(eval_expr)
            stack.append(str(res))

        else:
            stack.append(char)

    eval_expr = ""
    for val in stack:
        eval_expr += val

    return calculate2(eval_expr)

def read_input2(path:str)->dict:

    sum = 0

    txt_file = Path(path)
    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace("\n","")

            sum += eval_expression2(raw_line)

    return sum

res = read_input2("./input.txt")
print(res)