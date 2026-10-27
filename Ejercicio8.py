points = [10, -5, 20, -3, 15] 
totalin = 0 

for p in points:
    if p < 0:
        continue
    print("Puntos ganados", p)
    totalin += p

print("Total:", totalin)