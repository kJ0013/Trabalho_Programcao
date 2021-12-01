def executar():
    opcao='a'
    while opcao!='d':
        opcao = input('Qual Aeronave?: [a]->Legacy 500 [b]->Phenom 100 [c]-> Bandeirantes [d]->Voltar ')
        if opcao=='a':
            Remove=['Trem de Pouso','Tubo de Pitot','Entrada de Ar do motor','Antena', 'Motor',\
        'Escapamentos','Travas de Comando','Entrada de Ar do motor']
            print('Tags a serem verificadas!')
            print(Remove [0])
            print(Remove [1])
            print(Remove [2])
            print(Remove [3])
            print(Remove [4])
            print(Remove [5])
            print(Remove [6])
            opcao='a'
            opcao=input('[a]->Removido [b]->Colocado ')
            if opcao=='a':
                file = open('Legacy_500.txt','w+')
                file.write('As tags foram removidas com sucesso\n')
                file.write('Na aeronave Legacy')
                file.seek(0,0)
                print (file.read())
                file.close()
                pausa = input('Pressione Enter para voltar...')                
            elif opcao=='b':
                 file = open('Legacy_500.txt','w+')
                 file.write('As tags foram colocadas com sucesso\n')
                 file.write('Na aeronave Legacy')
                 file.seek(0,0)
                 print (file.read())
                 file.close()
                 pausa = input('Pressione Enter para voltar...')        
            else:
                print('Opção Inválida, por favor selecione uma opção válida')
                
                       
            
        elif opcao=='b':
            Remove=['Trem de Pouso','Tubo de Pitot','Entrada de Ar do motor','Antena', 'Motor',\
        'Escapamentos','Travas de Comando']
            print('Tags a serem verificadas!')
            print(Remove [0])
            print(Remove [1])
            print(Remove [2])
            print(Remove [3])
            print(Remove [4])
            print(Remove [5])
            print(Remove [6])
            opcao='a'
            opcao=input('[a]->Removido [b]->Colocado ')
            if opcao=='a':
                file = open('Phenom_100.txt','w+')
                file.write('As tags foram removidas com sucesso\n')
                file.write('Na aeronave Phenom')
                file.seek(0,0)
                print (file.read())
                file.close()
                pausa = input('Pressione Enter para voltar...')
            elif opcao=='b':
                file = open('Phenom_100.txt','w+')
                file.write('As tags foram colocadas com sucesso\n')
                file.write('Na aeronave Phenom')
                file.seek(0,0)
                print (file.read())
                file.close()
                pausa = input('Pressione Enter para voltar...')
            else:
                print('Opção Inválida, por favor selecione uma opção válida')

            

        elif opcao=='c':
            Remove=['Trem de Pouso','Tubo de Pitot','Entrada de Ar do motor','Antena', 'Motor',\
        'Escapamentos','Travas de Comando']
            print('Tags a serem verificadas!')
            print(Remove [0])
            print(Remove [1])
            print(Remove [3])
            print(Remove [5])
            print(Remove [6])
            opcao='a'
            opcao=input('[a]->Removido [b]->Colocado ')
            if opcao=='a':
                 file = open('Bandeirantes.txt','w+')
                 file.write('As tags foram colocadas com sucesso\n')
                 file.write('Na aeronave Bandeirantes')
                 file.seek(0,0)
                 print (file.read())
                 file.close()
                 pausa = input('Pressione Enter para voltar...')
            elif opcao=='b':
                 file = open('Legacy_500.txt','w+')
                 file.write('As tags foram colocadas com sucesso\n')
                 file.write('Na aeronave Legacy')
                 file.seek(0,0)
                 print (file.read())
                 file.close()
                 pausa = input('Pressione Enter para voltar...')       
            else:
                print('Opção Inválida, por favor selecione uma opção válida')
                


        elif opcao=='d':
            print('Voltando...')
        else:
            print('Opção Inválida, por favor selecione uma opção válida')




def ajuda():
    print('O program consiste em orientar o mecânico de onde se localizam as tags "remove before flight" nas aeronaves:Legacy e Phenom, e da a opção ao mecânico de marcar como removido ou colocado')
    pausa = input('Pressione Enter para voltar...')      

            
    
