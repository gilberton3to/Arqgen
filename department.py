# Função para criar um banco de dados simples em um arquivo de texto

def add_department(arquivo_nome):
    # Dados da empresa
    departamentos = [
        # Controle de departamentos: nome / number / gerente / sede
        "01, Urbanismo, 088.000.903-01, Fortaleza\n",
        "02, Paisagismo, 023.000.203-03, Fortaleza\n"
    ]

    # Abre o arquivo de texto para escrita
    with open(arquivo_nome, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(departamentos)
    
    print(f'Banco de dados {arquivo_nome} criado com sucesso!')

# Criar o banco de dados em formato texto
add_department('department.txt')

# Função para adicionar informações a um banco de dados simples em um arquivo de texto
def update_department(arquivo_nome, number, name, manager, headquarter):
    # Dados a serem adicionados
    new_info = f"{number}, {name}, {manager}, {headquarter}\n"
    
    # Abre o arquivo em modo de acréscimo ('a') para adicionar novas informações
    with open(arquivo_nome, 'a', encoding='utf-8') as arquivo:
        arquivo.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_department('department.txt', "01", "Urbanismo", '088.000.903-01', "Fortaleza")

# Função para exibir os departamentos
def show_department(arquivo_nome):
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # Dividindo a linha em partes e formatando a exibição
                number, name, manager, headquarter = linha.strip().split(', ')
                print(f'Numero: {number}, Nome: {name}, Gerente: {manager}, Sede: {headquarter}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_nome} não foi encontrado.')

# Exibir os departamentos
show_department('department.txt')
