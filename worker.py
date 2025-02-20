# Função para criar um banco de dados simples em um arquivo de texto

def add_worker(arquivo_nome):
    # Dados da empresa
    workers = [
        # Nome / CPF / Cargo / Endereço / Salário / Gênero / Nascimento / Formação / Department
        "João, 324.345.678-89, Gerente, Rua D, 8.0000, M, 09/03/1979, Superior, 1\n",
        "Maria, 234.765.356-98, Analista, Rua Felizberto, 12.0000, F, 23/12/2003, Superior incompleto, 2\n",
        "Pedro, 924.275.634-73, Supervisor, Rua Felizberto, 9.0000, M, 23/12/2003, Superior, 3\n"
    ]
    
    # Abre o arquivo de texto para escrita
    with open(arquivo_nome, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(workers)
    
    print(f'Banco de dados {arquivo_nome} criado com sucesso!')

# Criar o banco de dados em formato texto
add_worker('workers.txt')

# Função para adicionar informações a um banco de dados simples em um arquivo de texto
def update_worker(arquivo_nome, name, cpf, position, address, salary, gender, birth, formation, department):
    # Dados a serem adicionados
    new_info = f"{name}, {cpf}, {position}, {address}, {salary}, {gender}, {birth}, {formation}, {department}\n"
    
    # Abre o arquivo em modo de acréscimo ('a') para adicionar novas informações
    with open(arquivo_nome, 'a', encoding='utf-8') as arquivo:
        arquivo.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_worker('workers.txt', 'Ana', "765.234.356-98", "Gerente", "Rua Farias", "14.000", "F", "23/12/2003", "Superior", "1")

def show_workers(arquivo_nome):
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # Dividindo a linha em partes e formatando a exibição
                name, cpf, position, address, salary, gender, birth, formation, department = linha.strip().split(', ')
                print(f'Nome: {name}, CPF: {cpf}, Cargo: {position}, Endereço: {address}, Salário: {salary}, Gênero: {gender}, Nascimento: {birth}, Formação: {formation}, Department: {department}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_nome} não foi encontrado.')

show_workers('workers.txt')