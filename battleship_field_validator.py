# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

from pprint import pprint


battleField = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


from pprint import pprint


def validate_battlefield(field):
    pprint(field)
    
    battleship_count = 1
    cruiser_count = 1
    destroyer_count = 3
    submarine_count = 4
    
    def mark_as_cheked(i1, j1, i2, j2):
        direction = ''
        if (i2 - i1) == 0:
            direction = 'horizontal'
            i2 += 1
        if (j2 - j1) == 0:
            direction = 'vertical'
            j2 += 1
        for i in range(i1-1, i2+1):
            for j in range(j1-1, j2+1):
                field[i][j] = 7
                if direction == 'horizontal':
                    try:
                        field[i-1][j] = 4
                    except:
                        pass
                    try:
                        field[i+1][j] = 4
                    except:
                        pass
                if direction == 'vertical':
                    try:
                        field[i][j-1] = 4
                    except:
                        pass
                    try:
                        field[i][j+1] = 4
                    except:
                        pass
    
    def detect_direction(i, j):
        if field[i][j+1] == 1:
            return 'horizontal'
        if field[i+1][j] == 1:
            return 'vertical'
        return 'single'
    
    
    def get_ship_size(i,j):
        ship_direction = detect_direction(i,j)
        if ship_direction == 'single':
            return i, j, i, j
        if ship_direction == 'vertical':
            size = 0
            for n in range(i, len(field)):
                if field[n][j] == 1:
                    size += 1
                else:
                    return i, j, i + size, j 
        if ship_direction == 'horizontal':
            size = 0
            for n in range(j, len(field[0])):
                if field[i][n] == 1:
                    size += 1
                else:
                    return i, j, i, j + size
    
    def is_ship_perimetr_clean(i1, j1, i2, j2):
        for i, line in enumerate(field[j1:j2+1]):
            for j, val in enumerate(line[i1:i2+1]):
                print(val)
        return True
    
    
    for i, line in enumerate(field):
        for j, val in enumerate(line):
            if val == 1:
                ship_size = get_ship_size(i,j)
                if not is_ship_perimetr_clean(*ship_size):
                    return False
                mark_as_cheked(*ship_size)
                print('-'*30)
                pprint(field)
    
    
    return True

if __name__ == '__main__':
    print(f"{validate_battlefield(battleField)=}")
