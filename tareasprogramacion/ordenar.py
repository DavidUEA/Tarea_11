def sort_i(valores_numericos, ordenar):
    if ordenar < 0 or ordenar >= len(valores_numericos):
        print("indice de fila fuera de rango")
        return

    valores_numericos[ordenar] = sorted(valores_numericos[ordenar])

valores_numericos =[
    [8,5,9],
    [7,3,2],
    [4,1,6]
]
ordenar = 2
print("Matriz planteada")
for i in valores_numericos:
    print(i)




sort_i(valores_numericos, ordenar)

print("\nMatriz ordenada la fila", ordenar, "en orden ")
for i in valores_numericos:
    print(i)