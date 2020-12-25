
def get_loop_size(key, subj_num):

    val = 1
    loop = 0
    while val != key:
        loop += 1
        val = (val * subj_num) % 20201227
    return loop

def transform(key, loop_size):

    val = 1
    for _ in range(loop_size):
        val = (val * key) %  20201227
    return val

subj_num = 7
div_value = 20201227
card_key = 14082811
door_key = 5249543

card_loop_size = get_loop_size(card_key, subj_num)
door_loop_size = get_loop_size(door_key, subj_num)

res = transform(door_key, card_loop_size)
print(res)