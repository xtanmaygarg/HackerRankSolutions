area = dict()
for i in range(1, 101):
    area[i] = 4 * i + 2

H, W = map(int, input().split())
Figure = []
for i in range(H):
    Figure.append(list(map(int, input().split())))

finalArea = 0

for i in range(H):
    for j in range(W):
        if i == 0 and i == H - 1:
            if j == 0 and j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                finalArea += Curr
            elif j == 0:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i][j + 1])
                finalArea += Curr
            elif j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i][j - 1])
                finalArea += Curr
            else:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i][j - 1]) - min(Num, Figure[i][j + 1])
                finalArea += Curr            
        elif i == 0:
            if j == 0 and j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j])
                finalArea += Curr
            elif j == 0:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
            elif j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i][j - 1])
                finalArea += Curr
            else:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i][j - 1]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
        elif i == H - 1:
            if j == 0 and j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i - 1][j])
                finalArea += Curr
            elif j == 0:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
            elif j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j - 1])
                finalArea += Curr
            else:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j - 1]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
        else:
            if j == 0 and j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i - 1][j])
                finalArea += Curr
            elif j == 0:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
            elif j == W - 1:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j - 1])
                finalArea += Curr
            else:
                Num = Figure[i][j]
                Curr = area[Num]
                Curr = Curr - min(Num, Figure[i + 1][j]) - min(Num, Figure[i - 1][j]) - min(Num, Figure[i][j - 1]) - min(Num, Figure[i][j + 1])
                finalArea += Curr
print(finalArea)
            
