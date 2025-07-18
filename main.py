from funcs import *



# comprimento da senha que o usuário irá pedir
comprimento_da_senha = int(input("Comprimento da senha: "))


# a senha gerada
senha = gera_senha_forte(comprimento_da_senha)


# imprime a senha
print(senha)


