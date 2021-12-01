from model import executar,ajuda

opcao= '1'

while opcao!='3': 
    
    opcao = input('O que deseja?: [1]->Executar  [2]->Ajuda  [3]->sair ')

    if opcao=='1':
        executar()
        
    elif opcao=='2':
        ajuda()
        
        

    elif opcao=='3':
        print('Saindo...')

    else:
        print('Por favor selecione uma das opções válidas')
