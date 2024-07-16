before = [
    [0,0,0,0,0,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,0,0],
]

filter = [-1,0,1]

result = []

for row in range(len(before)):
    result_row = []
    for col in range(len(before[row])):
        if col == 0:
            selected = [before[row][col], before[row][col], before[row][col+1]]
        elif col == len(before[row])-1:
            selected = [before[row][col-1], before[row][col], before[row][col]]
        else:
            selected = [before[row][col-1], before[row][col], before[row][col+1]]
        calculated_point = selected[0] * filter[0]
        calculated_point += selected[1] * filter[1]
        calculated_point += selected[2] * filter[2]
        result_row.append(abs(calculated_point))
    result.append(result_row)

for row in result:
    print(row)
