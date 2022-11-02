"""
Undo e Redo
Data: 24/01/2022

Lista de tarefas
Faça uma lista de tarefas com as seguintes opções:
- adicionar tarefa
- listar tarefa
- opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
- opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""

lista_tarefas = []
tarefas_desfeitas = []
processo_finalizado = False

while processo_finalizado == False:

    print(
        'Opções:\n' +
        'Digite nova Tarefa\n' +
        'Digite "T" para visualizar lista de tarefas\n' +
        'Digite "F" para finalizar processo\n'
    )
    nova_tarefa = str(input("Escolha: "))

    if nova_tarefa == "F":
        processo_finalizado = True
    elif nova_tarefa != "T":
        lista_tarefas.append(nova_tarefa)
    else:
        retornar_menu = False
        while retornar_menu == False:
            print(lista_tarefas)
            print(
                '\n \nOpções:\n' +
                '"M" para retornar ao menu inicial\n' +
                '"D" para desfazer a última tarefa\n' +
                '"R" para refazer a última tarefa desfeita'
            )
            opcao = str(input("Opção escolhida: "))
            if opcao == "D" and lista_tarefas != []:
                tarefas_desfeitas.append(lista_tarefas[len(lista_tarefas) - 1])
                lista_tarefas.pop()
                print('Tarefas desfeitas:')
                print(tarefas_desfeitas)
                print('#' * 20)
            elif opcao == "D":
                print("Lista de tarefas não tem nenhum argumento para ser removido.")
            elif opcao == "R" and tarefas_desfeitas != []:
                lista_tarefas.append(tarefas_desfeitas[len(tarefas_desfeitas) - 1])
                tarefas_desfeitas.pop()
                print('Tarefas desfeitas:')
                print(tarefas_desfeitas)
                print('#' * 20)
            elif opcao == "R":
                print("Nenhuma tarefa está na lista de tarefas desfeitas.")
            elif opcao == "M":
                retornar_menu = True





