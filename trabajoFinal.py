"""
trabajoFinal.py
Autor: Tu Nombre
Fecha: 2025-07-16
Descripción: Script para el cálculo de comisiones en HGM SAC.
"""
import pandas as pd
df = pd.read_csv("archivos\\REGISTO VENTAS ENERO 2025 PAGO COMISIONES.CSV")

def calculoComision(montoTotal):
    monto_comision = 0
    if montoTotal > 20000:
        monto_comision = montoTotal * 0.10
    elif montoTotal> 15000:
        monto_comision = montoTotal * 0.075
    elif montoTotal> 10000:
        monto_comision = montoTotal * 0.05
    return monto_comision
    
def sumaTotalVentas(dataframe,codvend):
    suma_v01 = 0
    
    for index, fila in dataframe.iterrows():
        if fila["codigo"] == codvend and fila["estado"] == "CANCELADO":
            suma_v01 += fila["subtotal"]
    
    return suma_v01

#totalventav01 = sumaTotalVentas(df,"V01")
#comision_v01 = calculoComision(totalventav01)

vendedor1 = sumaTotalVentas(df,"V01")
comivendedor1 = calculoComision(vendedor1)
vendedor2 = sumaTotalVentas(df,"V02")
comivendedor2 = calculoComision(vendedor2)
vendedor3 = sumaTotalVentas(df,"V03")
comivendedor3 = calculoComision(vendedor3)
vendedor4 = sumaTotalVentas(df,"V04")
comivendedor4 = calculoComision(vendedor4)
vendedor5 = sumaTotalVentas(df,"V05")
comivendedor5 = calculoComision(vendedor5)

promedioComision =(comivendedor1+comivendedor2+comivendedor3+comivendedor4+comivendedor5)/5

resultado = 0
codigovend = ""
codigovendedor = ""
if vendedor1>vendedor2:
    resultado = vendedor1
    codigovend = "V01 JUAN PEREZ"
    codigovendedor = "V01"
else:
    resultado = vendedor2
    codigovend = "V02 LUIS CAMPOS"
    codigovendedor = "V02"

if resultado>vendedor3:
    resultado = resultado
    codigovend = codigovend
else:
    resultado = vendedor3
    codigovend = "V03 CARLA TORRES"
    codigovendedor = "V03"

if resultado>vendedor4:
    resultado = resultado
    codigovend = codigovend
else:
    resultado = vendedor4
    codigovend = "V04 VERONICA RIVERA"
    codigovendedor = "V04"

if resultado>vendedor5:
    resultado = resultado
    codigovend = codigovend
else:
    resultado = vendedor5
    codigovend = "V05 CARLOS TAPIA"
    codigovendedor = "V05"

bonomontocomision = sumaTotalVentas(df,codigovendedor)
bonoCommision = bonomontocomision * 0.02

resultado2 = 0
codigovend2= ""
if vendedor1<vendedor2:
    resultado2 = vendedor1
    codigovend2 = "V01 JUAN PEREZ"
else:
    resultado2 = vendedor2
    codigovend2 = "V02 LUIS CAMPOS"

if resultado2<vendedor3:
    resultado2 = resultado2
    codigovend2 = codigovend2
else:
    resultado2 = vendedor3
    codigovend2 = "V03 CARLA TORRES"

if resultado2<vendedor4:
    resultado2 = resultado2
    codigovend2 = codigovend2
else:
    resultado2 = vendedor4
    codigovend2 = "V04 VERONICA RIVERA"

if resultado2<vendedor5:
    resultado2 = resultado2
    codigovend2 = codigovend2
else:
    resultado2 = vendedor5
    codigovend2 = "V05 CARLOS TAPIA"

print(f"Total Venta V01 JUAN PEREZ: {round(sumaTotalVentas(df,"V01"),2)} Comision: {round(calculoComision(sumaTotalVentas(df,"V01")),2)}")
print(f"Total Venta V02 LUIS CAMPOS: {round(sumaTotalVentas(df,"V02"),2)} Comision: {round(calculoComision(sumaTotalVentas(df,"V02")),2)}")
print(f"Total Venta V03 CARLA TORRES: {round(sumaTotalVentas(df,"V03"),2)} Comision: {round(calculoComision(sumaTotalVentas(df,"V03")),2)}")
print(f"Total Venta V04 VERONICA RIVERA: {round(sumaTotalVentas(df,"V04"),2)} Comision: {round(calculoComision(sumaTotalVentas(df,"V04")),2)}")
print(f"Total Venta V05 CARLOS TAPIA: {round(sumaTotalVentas(df,"V05"),2)} Comision: {round(calculoComision(sumaTotalVentas(df,"V05")),2)}")

print(f"El vendedor que vendio mas es: {codigovend} Monto: {resultado}")
print(f"El vendedor que vendio menos es: {codigovend2} Monto: {resultado2}")
print(f"Se dara un bono al vendedor que hizo mas ventas: {codigovend} Bono: {round(bonoCommision,2)}")
print(f"Promedio de comisión es: {round(promedioComision,2)}")
print("Proceso completado correctamente.")
