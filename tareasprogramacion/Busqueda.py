print("Matriz bidimensional")
valores_numericos =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

vle = 10
fila_en = -1
colum_en = -1

if any(vle in fila for fila in valores_numericos):
    print("Se encontro el numero", vle , "en valores_numericos")
else:
    print("no se encontro el numero", vle , "en la matriz")