from settings import *


def nearby_cells_count(cells: list, x: int, y: int):
    res = []
    if (x > 0) and (y > 0) and (x < cell_count-1) and (y < cell_count-1):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) != (x, y):
                    res.append(cells[i][j])
                    # print(res)
    if res.count(1) == None:
        return 0
    else:
        return res.count(1)


def nearby_cell_data(cells: list):
    data = []
    for i in range(cell_count):
        temp = []
        for j in range(cell_count):
            temp.append(0)
        data.append(temp)
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            data[x][y] = nearby_cells_count(cells, x, y)
    return data
