from random import randint

index_ = 0


class MineSweeper:
    @classmethod
    def createMineField(cls, size, mine):
        arr = [[0 for row in range(size)] for column in range(size)]

        for num in range(mine):  # 지뢰가 겹치는 경우가 생김
            x = randint(0, size - 1)
            y = randint(0, size - 1)
            # while True:
            #     if arr[y][x]:
            #         if arr[y][x] == "*":
            #             return True
            #         else:
            #             arr[y][x] = "*"
            #             return False
            #     else: print("--")

            if (x >= 0 and x <= size - 2) and (y >= 0 and y <= size - 1):
                if arr[y][x+1] != "*":
                    arr[y][x+1] += 1  # center right
            if (x >= 1 and x <= size - 1) and (y >= 0 and y <= size - 1):
                if arr[y][x-1] != "*":
                    arr[y][x-1] += 1  # center left
            if (x >= 1 and x <= size - 1) and (y >= 1 and y <= size - 1):
                if arr[y-1][x-1] != "*":
                    arr[y-1][x-1] += 1  # top left
            if (x >= 0 and x <= size - 2) and (y >= 1 and y <= size - 1):
                if arr[y-1][x+1] != "*":
                    arr[y-1][x+1] += 1  # top right
            if (x >= 0 and x <= size - 1) and (y >= 1 and y <= size - 1):
                if arr[y-1][x] != "*":
                    arr[y-1][x] += 1  # top center
            if (x >= 0 and x <= size - 2) and (y >= 0 and y <= size - 2):
                if arr[y+1][x+1] != "*":
                    arr[y+1][x+1] += 1  # bottom right
            if (x >= 1 and x <= size - 1) and (y >= 0 and y <= size - 2):
                if arr[y+1][x-1] != "*":
                    arr[y+1][x-1] += 1  # bottom left
            if (x >= 0 and x <= size - 1) and (y >= 0 and y <= size - 2):
                if arr[y+1][x] != "*":
                    arr[y+1][x] += 1  # bottom center


            for py in range(y-1,y+2):
                for px in range(x-1, x+2):
                    if py != y or px != x: continue
                    if py < 0 or py >= size  \
                            or px < 0 or px >= size : continue
                    arr[py][px] += 1


        for row in arr:
            print("\t".join(str(cell) for cell in row))
            # print("")



ms = MineSweeper.;
ms.createMineField()