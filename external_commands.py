"""
External Commands
14/02/2022

Como executar comandos externos no python.
É necessário utilizar o módulo subprocess
"""
import subprocess

# Windows - ping 127.0.0.1

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True  # Quando fazemos isso, a saída do comando
    # vai para a variável ao inves do console
)

print(proc.stderr)  # Mostra os error
print(proc.stdout)  # Mostra a saída do comando
print(proc.returncode)  # Mostra o código
# Isso é muito útil

# O 'b' é no formato de bytes. Para ter a saída em modo texto
print('\n' * 3)
# Para colocar em texto
proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

print(proc.stdout)
