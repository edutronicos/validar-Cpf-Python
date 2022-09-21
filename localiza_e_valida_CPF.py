import re

def validaCpf(cpf):             #Função para validar CPF.
    cpf = list(map(int, cpf))   #Transforma a lista de string em lista de inteiro.

    if cpf[0] == cpf[1] and cpf[1] == cpf[2] and cpf[2] == cpf[3] and cpf[3] == cpf[4] and cpf[4] == cpf[5] and cpf[5] == cpf[6] and cpf[6] == cpf[7] and cpf[7] == cpf[8] and cpf[8] == cpf[9] and cpf[9] == cpf[10]:
        return False

    else:
        soma1 = cpf[0]*10 + cpf[1]*9 + cpf[2]*8 + cpf[3]*7 + cpf[4]*6 + cpf[5]*5 + cpf[6]*4 + cpf[7]*3 + cpf[8]*2               #Soma pra validar o primeiro numero depois do -
        resto1 = soma1*10%11

        if resto1 == 10:    #Verfica se o resto da conta é 10. 
            resto1 = 0      #Se for 10, atribui 0 para variavel.

        soma2 = cpf[0]*11 + cpf[1]*10 + cpf[2]*9 + cpf[3]*8 + cpf[4]*7 + cpf[5]*6 + cpf[6]*5 + cpf[7]*4 + cpf[8]*3 + cpf[9]*2   #Soma pra validar o segundo numero depois do -
        
        resto2 = soma2*10%11
        if resto2 == 10:    #Verfica se o resto da conta é 10. 
            resto2 = 0      #Se for 10, atribui 0 para variavel.

        if resto1 == cpf[9] and resto2 == cpf[10]:      #Verifica se o resto é igual aos numeros depois do -
            return True     #Retorna True para verdadeiro
        else:
            return False    #Se não for verdadeiro retorna False.


texto = 'Fulano tem o cpf 111.111.111-22'                              #Texto ou pode ser um Input.
padrao_cpf = re.compile(r'\d{3}.\d{3}.\d{3}.\d{2}|\d{11}|\d{9}.\d{2}')  #Padrão regex para encontrar cpf digitado de varias formas em e-mails.
loc = padrao_cpf.findall(texto)                                         #Findall retorna uma lista com as strings encontradas

for li in loc:                                          #Imprime uma lista com as strings uma em baixo da outra.
    teste = li
    resultado = re.sub(r'[\s._:;*+-\/\\]', '', teste)   #Retira do CPF os caracteres inseridos dentro dos []
    cpf = list(resultado)                               #Transforma a variavel resultado em uma lista, separando os numeros do CPF
    valida = validaCpf(cpf)                             #Guarda o resultado da função validaCpf() dentro da variavel
    
    if valida == True:                                  #Verifica se o resultado dentro da variavel se é Verdadeiro ou Falso
        print(f'{teste} correto')
    else:
        print(f'{teste} falso')