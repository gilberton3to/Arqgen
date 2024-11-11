# Função para criar um banco de dados simples em um arquive de texto
def add_worker(arquive_name):
    # Dados Empresa 
    workers = [
        # Nome/CPF/endereco/salario/genero/nascimento
        "João, 324.345.678-89, Rua D, 8.0000, M, 09/03/1979\n",
        "Maria, 234.765.356-98, Rua Felizberto, 12.0000, F, 23/12/2003\n",
        "Pedro, 924.275.634-73, Rua Felizberto, 9.0000, M, 23/12/2003\n"
    ]
    
    # Abre o arquive de texto para escrita
    with open(arquive_name, 'w', encoding='utf-8') as arquive:
        arquive.writelines(workers)
    
    print(f'Banco de dados {arquive_name} criado com sucesso!')

# Criar o banco de dados em formato texto
add_worker('workers.txt')

# Função para adicionar informações a um banco de dados simples em um arquive de texto
def update_worker(arquive_name, name, cpf, address, salary, gender, birth):
    # Dados a serem adicionados
    new_info = f"{name}, {cpf}, {address}, {salary}, {gender}, {birth}\n"
    
    # Abre o arquive em modo de acréscimo ('a') para adicionar novas informações
    with open(arquive_name, 'a', encoding='utf-8') as arquive:
        arquive.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_worker('workers.txt', 'Ana', "765.234.356-98", "Rua Farias", "14.000", "F", "23/12/2003")

def show_workers(arquive_name):
    try:
        with open(arquive_name, 'r', encoding='utf-8') as arquive:
            lines = arquive.readlines()
            for line in lines:
                # Dividindo a linha em partes e formatando a exibição
                name, cpf, address, salary, gender, birth = line.strip().split(', ')
                print(f'Nome: {name}, CPF: {cpf}, Endereco: {address}, Salario: {salary}, Genero: {gender}, Nascimento: {birth}')
    except FileNotFoundError:
        print(f'O arquive {arquive_name} não foi encontrado.')

show_workers('workers.txt')
