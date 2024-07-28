import os


def limpa_tela():
    os.system('cls')


def exibir_menu_principal():
    limpa_tela()
    print('Calculadora Simples\n')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('s. Sair\n')


def voltar_ao_menu():
    input('Aperte qualquer tecla para continuar: ')


def calculadora():
    while True:
        try:
            exibir_menu_principal()

            opcao_escolhida = input('Digite a opção que deseja ("s" para sair): ')
            if opcao_escolhida == 's' or opcao_escolhida == 'S':
                limpa_tela()
                print('Obrigado por usar a Calculadora Simples!')
                break

            if opcao_escolhida not in ['1', '2', '3', '4']:
                print('\nEsta opção não é válida. Tente novamente.')
                voltar_ao_menu()
                continue

            valor_1 = float(input('Digite o primeiro número: '))
            valor_2 = float(input('Digite o segundo número: '))

            match opcao_escolhida:
                case '1':
                    operacao = 'soma'
                    calculo = valor_1 + valor_2
                case '2':
                    operacao = 'subtração'
                    calculo = valor_1 - valor_2
                case '3':
                    operacao = 'multiplicação'
                    calculo = valor_1 * valor_2
                case '4':
                    operacao = 'divisão'
                    if valor_2 == 0:
                        raise ZeroDivisionError('Não é possível realizar a divisão por zero.')
                    else:
                        calculo = valor_1 / valor_2
        except ValueError:
            print(f'\nValor incorreto! Insira corretamente um número para ser realizada a operação.')
            voltar_ao_menu()
        except Exception as e:
            print(f'{type(e)} {e}')
            voltar_ao_menu()
        else:
            print(f'\nO resultado da {operacao} é: {calculo}\n')
            voltar_ao_menu()


calculadora()
