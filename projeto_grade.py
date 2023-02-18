def desenha_linha():
    print('+',end='')
    for i in range(15):
        print('-',end='')
    print('+',end='')
    for i in range(6):
        for j in range(10):
            print('-',end='')
        print('+',end='')
    print()


def cabecalho():
    desenha_linha()
    print('|',' '*15,'|',end='',sep='')
    
    
    for i in range(6):
        dia = dias_matriz[i]
        
        print(f' {dia}',' '*6,'|', end='',sep='')

    print()
    desenha_linha()


def atualiza_matriz(grade, instrucao):
    def periodo(periodo):
        if 'M' in periodo:
            return 0
        elif 'T' in periodo:
            return 1
        else:
            return 2
    lista = instrucao.split(' ')
    add_sub = lista[0]
    aula = lista[1]
    horarios = lista[2:]

    for horario in horarios:
        divisao = 0
        alocacao = 0
        if periodo(horario)==0:
            divisao = horario.find('M')
            alocacao = -1
        elif periodo(horario) == 1:
            divisao = horario.find('T')
            alocacao = 4
        else:
            divisao = horario.find('N')
            alocacao = 10

        dias = horario[:divisao]
        hora = horario[divisao+1:]

        for dia in dias:
            for num in hora:
                linha = int(num) + alocacao #horario
                coluna = int(dia) - 2 #dia
                if add_sub == '+':
                    if grade[linha][coluna]!='': 
                        erro = f'!({instrucao})'
                        return erro
                else:
                    if grade[linha][coluna] != aula:
                        erro =  f'!({instrucao})'
                        return erro

        for dia in dias:
            for num in hora:
                linha = int(num) + alocacao #horario
                coluna = int(dia) - 2 #dia
                if add_sub == '+':
                    grade[linha][coluna] = aula
                else:
                    grade[linha][coluna] = ''


def mostra_grade(grade):
    def relogio(index):
        return horarios_matriz[index]
        

    def linha_vazia(linha):
        for elemento in linha:
            if elemento!='':
                return False
        return True
    
    cabecalho()
    
    i = 0
    for linha in grade:
        if not linha_vazia(linha):
            print(f'| {relogio(i)} |',end='')
            for elemento in linha:
                if elemento!='':
                    print(f' {elemento[:8]} |',end='')
                else:
                    print(' '*9,'|',end='')
            print()
            desenha_linha()
        i+=1

grade = []
horarios_matriz = {0:'08:00 - 08:55',1:'08:55 - 09:50',2:'10:00 - 10:55',3:'10:55 - 11:50',4:'12:00 - 12:55',
        5:'12:55 - 13:50', 6:'14:00 - 14:55',7:'14:55 - 15:50',8:'16:00 - 16:55',9:'16:55 - 17:50',10:'18:00 - 18:55',
        11:'19:00 - 19:50', 12:'19:50 - 20:40', 13:'20:50 - 21:40', 14:'21:40 - 22:30'}

dias_matriz = {0:'Seg',1:'Ter',2:'Qua',3:'Qui',4:'Sex',5:'Sab'}

for i in range(15):
    linha = []
    for j in range(6):
        linha.append('')
    grade.append(linha)

erros = []
instrucao = input()



while instrucao!='Hasta la vista, beibe!':
    if instrucao!='?':
        erro = atualiza_matriz(grade,instrucao)
        if erro not in erros and erro!=None:
            erros.append(erro)
    else:
        for erro in erros:
            print(erro)
        erros = []
        mostra_grade(grade)

    instrucao = input()


 #+ CIC00003 35T23       

    
    

    






