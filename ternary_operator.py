"""
Operador Ternário
Data: 26/12/2021
"""
user_logged = True

if user_logged:
    message = "Usuário Logado."
else:
    message = "Login Necessário."

# Com operador ternário
user_logged = input('Usuário Logado? [Y/N] ')
user_logged = True if user_logged == 'Y' else False
message = "Usuário Logado." if user_logged else "Login Necessário."
print(message)