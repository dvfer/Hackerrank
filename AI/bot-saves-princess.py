def displayPathtoPrincess(n, grid):
    half = int(n/2)
    botCoords = (half, half)
    princessCoords = princessCoord(n, grid)
    print("\n".join(equalX(botCoords,princessCoords)))
    print("\n".join(equalY(botCoords,princessCoords)))
    
    
def equalX(botCoords, princessCoords):
    _, Xbot = botCoords
    _,Xprincess = princessCoords

    Xmoves = []
    diference = Xbot - Xprincess
    return ["RIGHT" if diference < 0 else "LEFT" for _ in range(abs(diference))]
    # while (Xbot != Xprincess):
    #     if (Xbot < Xprincess):
    #         Xbot+=1
    #         Xmoves.append("RIGHT")
    #     elif (Xbot > Xprincess):
    #         Xbot -= 1
    #         Xmoves.append("LEFT")
    # return Xmoves
def equalY(botCoords, princessCoords):
    Ybot, _ = botCoords
    Yprincess, _ = princessCoords
    Ymoves = []
    diference = Ybot - Yprincess
    # while (Ybot != Yprincess):
    #     if (Ybot < Yprincess):
    #         Ybot+=1
    #         Ymoves.append("DOWN")
    #     elif (Ybot > Yprincess):
    #         Ybot -= 1
    #         Ymoves.append("UP")
    # return Ymoves
    return ["DOWN" if diference < 0 else "UP" for _ in range(abs(diference)) ]



def princessCoord(n, grid):
    if grid[0][0] == "p":
        return (0,0)
    elif grid[0][n-1] == "p":
        return (0, n-1)
    elif grid[n-1][0] == "p":
        return (n-1, 0)
    elif grid[n-1][n-1] == "p":
        return (n-1,n-1)

m = int(input())
grid = []
for i in range(0,m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)

