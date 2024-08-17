def calcular_promediolist(lista_num):
    longitud=len(lista_num)
    sumatoria=0
    for elemento in lista_num:
        sumatoria=sumatoria+elemento
    
    promedio=sumatoria/longitud
    return promedio

mi_lista=[5,8,23,14,55,17]

print(calcular_promediolist(mi_lista))

