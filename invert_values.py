"""
Inverter os Valores das Variáveis
Data: 26/12/2021
"""
# Forma convencional de inverter valores ----
x = 2
y = 3
# Trocar x com y.
z = x
x = y
y = z
print(f'x: {x}; y: {y}.')

# Inverter valores no python
x = 2
y = 3
y, x = x, y
print(f'x: {x}; y: {y}.')

# Para três variáveis
x = 2
y = 3
z = 4

x, y, z = y, z, x
print(f'x: {x}; y: {y}; z: {z}.')