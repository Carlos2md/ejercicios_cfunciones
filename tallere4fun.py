def calcular_factura(valor, iva=21):
    total=valor+(valor*(iva/100))
    return total
con_sin_iva=input("Ingrese 'si', o 'no' desea calcular la factura con iva: ")

if con_sin_iva=='si':
    try:
        valor=float(input("Por Favor Ingrese el valor de la Factura: "))
        iva=int(input("Por Favor ingrese el valor del iva: "))
        print(f"El valor total de la factura es {calcular_factura(valor,iva)}")
    
    except Exception as e:
        print("Valores No Validose",e)

elif con_sin_iva=='no':
    try:
        valor=float(input("Por Favor Ingrese el valor de la Factura: "))
        print(f"El valor total de la factura es {calcular_factura(valor)}")
    
    except Exception as e:
        print("Valores No Validose",e)

else:
    print("Opcion no Valida")

