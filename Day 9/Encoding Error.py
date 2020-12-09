from pathlib import Path

def read_input(path:str)->list:

    numbers = []

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')
            numbers.append(int(raw_line))

    return numbers

def sum_of_two(array:list, sum:int)->bool:

    complements = {}

    for item in array:

        if complements.get(item) != None:
            return True
        complements[sum-item] = item

    return False

def find_invalid_number(array:list, offset:int)->int:

    for ind in range(offset, len(numbers)):
        cur_number = array[ind]
        temp_array = array[ind - offset:ind]

        is_sum = sum_of_two(temp_array, cur_number)

        if not is_sum:
            return cur_number

    return 0

def find_contiguous_set(array:list, number:int)->list:

    current_set = []
    for index in range(len(array)):

        current_sum = sum(current_set)

        if current_sum == number:
            return current_set

        current_set.append(array[index])
        current_sum = sum(current_set)

        if current_sum > number:
            temp_sum = current_sum
            #deleting elements from the left side of current set
            while temp_sum > number:
                current_set.pop(0)
                temp_sum = sum(current_set)



# numbers = read_input("./test_input.txt")
# offset = 5
numbers = read_input("./input.txt")
offset = 25

invalid_number = find_invalid_number(numbers, offset)
print(invalid_number)

contiguous_set = find_contiguous_set(numbers, invalid_number)
print(contiguous_set)

result = min(contiguous_set) + max(contiguous_set)
print(result)





