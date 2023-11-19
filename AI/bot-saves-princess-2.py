def nextMove(n,r,c,grid):
    princessCoord = princessCoords(n, grid)
    difference = (r - princessCoord[0] , c - princessCoord[1] )

    if abs(difference[0]) < abs(difference[1]):
        if(difference[1] > 0 ):
            return "LEFT"
        elif(difference[1] < 0 ):
            return "RIGHT"
    elif abs(difference[0]) < abs(difference[1]):
        if(difference[0] > 0 ):
            return "UP"
        elif(difference[0] < 0 ):
            return "DOWN"


def princessCoords(n, grid):
    for row, line in enumerate(grid):
        lineList = list(line)
        try:
            column = lineList.index("p")
            return (row, column)
        except:
            continue

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

# print(grid[r][c])
print(nextMove(n, r, c, grid))