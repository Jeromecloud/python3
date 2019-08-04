#遍历元组数字求和
def sum_num(*args):
    n = 0
    for n in args:
        n += n
    return n
print(sum_num(1,2,3))