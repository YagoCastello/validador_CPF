# #Validador de CPF
import sys
import re
while True:
    cpf=input('Por favor digite um cpf, ou digite "s" para sair: ')\
        .replace('.','')\
        .replace('-','')

    entrada_e_sequencial = cpf == cpf[0]*len(cpf)
    if entrada_e_sequencial:
        print('Você enviou dados sequencias')
        sys.exit()
    lista=[]
    contador=10
    contador_2=11
    multiplicacao=[]
    soma=soma_2=0
    if len(cpf)==11:
        try:
            if cpf.isdigit :
                for c in range(9):
                    lista.append(int(cpf[c]))
                
                for d in lista:
                    valor_multiplicacao=d*contador
                    multiplicacao.append(valor_multiplicacao) 
                    soma+= valor_multiplicacao
                    contador-=1

                resultado = (soma *10)%11

            if resultado >9:
                lista.append(0)
            else:
                lista.append(resultado)
                      
            multiplicacao.clear
            for d in lista:
                valor_multiplicacao=d*contador_2
                multiplicacao.append(valor_multiplicacao) 
                soma_2+= valor_multiplicacao
                contador_2-=1

            resultado_2 = (soma_2 *10)%11

            if resultado_2 >9:
                lista.append(0)
            else:
                lista.append(resultado_2)
            palavra=''
            for n in lista:
                palavra+=str(n)
           
            def formatado(text):
                limpo=''
                for c in range(11):
                    if c == 2 or c == 5 :
                        limpo+=palavra[c]
                        limpo+='.'
                    elif c==8:
                        limpo+=palavra[c]
                        limpo+='-'
                    else:
                        limpo+=palavra[c]
                return limpo
            if cpf==palavra:
                print('cpf válido!!')
            else:
                print('cpf INválido!!')
            print(formatado(palavra))
                 
        except:
            print('SOMENTE NÚMEROS')
    elif cpf=='s':
        break  
    else:
        print('CPF INVÁLIDO')

print('FIM!!')
