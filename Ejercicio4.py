suma =  0

for i in range(3):
    nota = float(input("Ingrese una nota:"))
    suma += nota

promedio = suma / 3
print("Tu promedio es promedio:", promedio)

if promedio >= 3.0:
    print("Aprobaste de paso")
else:
    print("Reprobaste chavalín")