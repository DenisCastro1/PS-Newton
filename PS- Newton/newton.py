#exercício 1

def resumir(texto):
    
    lista=[]
    contador=0
    texto_resumido=''
    
    for caractere in texto:
        contador+=1 # conta o numero de caracteres do texto
        lista.append(caractere) #adiciona cada caractere numa lista vazia
        
        if contador>140:
            lista.append("...") # caso o contador resulte em um número acima de 140, há a adição dos três pontos 
            break
        
    for elemento in lista:
        texto_resumido=texto_resumido+elemento #adiciona cada caractere da lista em uma string através de concatenação
        
    return texto_resumido

#exercício 2
def digitos(numero):
    
    contador=0
    numero_string=str(numero)# transforma o numero numa string 
    
    for digito in numero_string:
        contador=contador+1 #conta quantos dígitos existem no "número"
        
    if contador==1: #caso o numero seja unitario (de 1 a 9)
        primeiro_digito=numero_string[0]
        primeira_casa_decimal="0"
        segunda_casa_decimal="0"
        unidade=''
        
    elif contador==2:# caso o numero tenha 2 dígitos (dezena)
        primeiro_digito=numero_string[0]
        primeira_casa_decimal=numero_string[1]
        segunda_casa_decimal="0"
        unidade="dezenas"
        
    else:# caso o numero tenha dezena ou centena (ex: dezena de milhar (23000))- OBS: é valido apenas para numeros de até 12 dígitos- centena de bilhão
        
        if contador/4==1: 
            unidade="mil"
        elif contador/7==1:
            unidade="milhão"
        elif contador/10==1:
            unidade="bilhão"
        elif contador%4==1:
            unidade="dezena de milhar"
        elif contador%4==2:
            unidade="centena de milhar"
        elif contador%7==1:
            unidade="dezena de milhão"
        elif contador%7==2:
            unidade="centena de milhão"
        elif contador%10==1:
            unidade="dezena de bilhão"
        elif contador%10==2:
            unidade="centena de bilhão"
        else:
            unidade=''
        primeiro_digito=numero_string[0]
        primeira_casa_decimal=numero_string[1]
        segunda_casa_decimal=numero_string[2]
        
        

    

    numero_final=primeiro_digito+","+primeira_casa_decimal+segunda_casa_decimal+" "+unidade
    numero_final_sem_unidade=primeiro_digito+","+primeira_casa_decimal+segunda_casa_decimal # retorna o número sem o nome da unidade,para ser utilizado no exercício 4
    
    return numero_final,numero_final_sem_unidade

#exercício 4
arquivo=open("sucessos_bilheteria.txt","r") # abre o arquivo no modo leitura

lista=arquivo.readlines() #cria uma lista com os dados do arquivo

#variaveis para os valores das bilheterias de cada ano
contador=0
valor1997=0
valor2013=0
valor2015=0
valor2018=0
valor2009=0
valor2017=0
valor2011=0
valor2019=0


#realiza a soma das bilheterias dos filmes de cada ano
for elemento in lista:
    
    separado=elemento.split(" ")
    índice_ultimo_elemento = len(separado)-1
    
    if separado[0]=="1997":
        valor1997=valor1997+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2013":
        valor2013=valor2013+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2015":
        valor2015=valor2015+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2018":
        valor2018=valor2018+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2009":
        valor2009=valor2009+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2017":
        valor2017=valor2017+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2011":
        valor2011=valor2011+float(separado[índice_ultimo_elemento])
    elif separado[0]=="2019":
        valor2019=valor2019+float(separado[índice_ultimo_elemento])
        
    
# chama a função do exercicio 2 para formatar o numero para 2 dígitos de casa decimal e printa na tela os valores da bilheteria de cada ano     
print("Valor arrecadado em 1997: U$ {} Bilhões ".format(digitos(valor1997)[1])) 
print("Valor arrecadado em 2013: U$ {} Bilhões".format(digitos(valor2013)[1]))
print("Valor arrecadado em 2015: U$ {} Bilhões".format(digitos(valor2015)[1]))
print("Valor arrecadado em 2018: U$ {} Bilhões".format(digitos(valor2018)[1]))
print("Valor arrecadado em 2009: U$ {} Bilhões".format(digitos(valor2009)[1]))
print("Valor arrecadado em 2017: U$ {} Bilhões".format(digitos(valor2017)[1]))
print("Valor arrecadado em 2011: U$ {} Bilhões".format(digitos(valor2011)[1]))
print("Valor arrecadado em 2019: U$ {} Bilhões".format(digitos(valor2019)[1]))

    
    


    
    
    
    
   
    
        
        





