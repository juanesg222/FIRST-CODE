# Diagrama de flujo diseñado en clase:
#  1. [Inicio] Inicio
#  2. [Entrada] Leer salario del empleado
#  3. [Repetición] Para cada uno de los 5 empleados
#  4. [Decisión] ¿salario < 2 SMMLV?
#  5. [Proceso] total = total + pago
#  6. [Salida] Mostrar el total de la nómina
#  7. [Fin] Fin

SMMLV = 1423500
AUXILIO = 200000
salarios = [1200000, 3500000, 1800000, 2600000, 1423500]

total = 0
for salario in salarios:          # REPETICIÓN
    pago = salario
    if salario < 2 * SMMLV:       # DECISIÓN
        pago += AUXILIO
    total += pago                 # SECUENCIA

print("Total nómina:", total)