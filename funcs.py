def gera_senha_forte(comprimento_requisitado_para_a_senha):
    '''-> Gera uma senha seguera de 12 caracteres ou mais

        Parâmetros:

            comprimento_requisitado_para_a_senha(int): o tamanho da senha que o usuário
            requisitou (se o tamanho for inferior a 12, é gerado uma senha de 12
            caracteres)

            return: retorna a senha gerada
    '''



    import string
    from random import choice




    senha = ''

    comprimento_minimo = 12


    # verifica se o tamanho de senha que o usuário pediu é de no mínimo 12
    #caracteres
    if comprimento_requisitado_para_a_senha < comprimento_minimo:

        comprimento_requisitado_para_a_senha = comprimento_minimo

    
    # pega uma lista com todas as letras maiúsculas
    letras_maiusculas = string.ascii_uppercase

    # pega uma lista com todas as letras minúsculas
    letras_minusculas = string.ascii_lowercase

    # pega uma lista com todas os números
    numeros = string.digits

    # pega uma lista com todos os caracteres especiais
    caracteres_especiais = string.punctuation


    # junta as 4 listas de caracteres em uma única lista chamada "caracteres"
    caracteres = [

    letras_maiusculas,

    letras_minusculas,

    numeros,

    caracteres_especiais
    ]

    

    # quantidade de dígitos adicionados à senha até o momento
    quantidade_de_digitos_adicionados_a_senha = 0


    # continua a execução até que a quantidade de dígitos adicionados a senha
    # seja igual ao tamanho de senha que o usuário pediu
    while quantidade_de_digitos_adicionados_a_senha < comprimento_requisitado_para_a_senha:


        # pega o caracter a ser adicionado a senha nessa iteração
        # é escolhido um valor aleatório da lista "caracteres" (letras maiúsculas,
        #letras minúsculas, números ou pontuações) e então de uma das 4 listas
        # escolhidas, é pego outo valor aleatório dessa lista, sendo esse o
        # caracter a ser adicionado à lista
        caracter_a_ser_adicionado = choice(choice(caracteres))


        # adicionado o caracter gerado à senha
        senha += caracter_a_ser_adicionado


        # um elemento foi adicionado a senha, logo é incrementado um valor 
        #para a quantidade de dígitos já adicinados à lista
        quantidade_de_digitos_adicionados_a_senha += 1


        # se a senha já tiver o tamanho requisitado pelo usuário, então é
        # verificado então se a senha é segura -> se a senha gerada tem ao menos
        # 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caracter especial
        if quantidade_de_digitos_adicionados_a_senha == comprimento_requisitado_para_a_senha:

            # verifica se a senha é segura
            senha_e_segura = verifica_se_senha_e_segura(senha)



            # se a senha não for segura, precisará ser gerada uma nova senha
            if not senha_e_segura:

                quantidade_de_digitos_adicionados_a_senha = 0

                senha = ''

    return senha



def verifica_se_senha_e_segura(senha):
    '''-> Verifica se uma senha é segura

        Parâmetros:

            senha(str): senha é ser verificada
            return: retorna "True" para caso a senha seja "segura" ou "False" para
            o caso de a senha "não ser segura"
    '''

    import string


    # pega uma lista com todas as letras minúsculas
    lista_letras_minusculas = string.ascii_lowercase

    # pega uma lsita com todas as letras maiúsculas
    lista_letras_maiusculas = string.ascii_uppercase

    # pega uma lista com todos os números
    lista_numeros = string.digits

    # pega uma lista com todos os caracteres especiais
    lista_caracteres_especiais = string.punctuation

    # variáveis que serão usadas para verificar se a senha é segura
    possui_letra_minuscula = possui_letra_maiuscula = possui_numero = False

    possui_caracter_especial = possui_12_caracteres = False


    # se a senha nem mesmo ao menos tiver 12 caracteres, a senha já não pode ser
    # considerada segura (a senha não é segura)
    if len(senha) < 12:

        return False
    
    # a senha é segura
    else:

        possui_12_caracteres = True


    # percorre a senha inteira, dígito por dígito, para verificar se há ao menos
    # uma letra minúscula, uma letra maiúscula, um número e ao menos um caracter
    # especial
    for digito in senha:

        if digito in lista_letras_minusculas:

            possui_letra_minuscula = True


        elif digito in lista_letras_maiusculas:

            possui_letra_maiuscula = True

        elif digito in lista_numeros:

            possui_numero = True


        elif digito in lista_caracteres_especiais:


            possui_caracter_especial = True



    # verifica se a senha cumpre todos os requisitos para ser considerada uma senha
    # segura
    senha_e_segura = possui_letra_maiuscula and possui_letra_minuscula and possui_numero and possui_caracter_especial


    # A senha é segura
    if senha_e_segura:

        return True

    # A senha não é segura
    else:

        return False