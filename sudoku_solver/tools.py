def print_p(p):
    print('-'*60)
    for line in p:
        print(line)


def copy_p(p):
    return [[i for i in line] for line in p]