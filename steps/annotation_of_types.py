# some func
# annotation of types args for comfort
def func(num: int, line: str):
    new_num = num * len(line)
    new_line = line * num
    return new_num, new_line

print(func(10, "lo"))