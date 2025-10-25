from dotenv import load_dotenv
from modules.api import conexao_api
from modules.processamento import extrair_dados
from modules.salvar_clima import salvar_em_json


def obter_cidade():
    print('\n=== Previsão do Tempo ===\n')
    while True:
        print('[1] - Ver temperarua | [2] - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cidade = input('\nInforme o nome da Cidade: ').strip()  

            if cidade:
                dados = conexao_api(cidade)
                if dados:
                    extrair_dados(dados)
                    salvar_em_json(cidade, dados)
            else:
                print('\nDigite o nome de uma cidade.\n')
                continue
        elif opcao == '2':
            print('Encerrando programa...')
            break
        
        else:
            print('Opção inválida. Tente novamente.\n')
        
if __name__ == "__main__":
    load_dotenv()
    obter_cidade()