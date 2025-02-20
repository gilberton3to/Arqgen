# Função para criar um banco de dados simples em um arquivo de texto

def add_project(arquivo_nome):
    # Dados da empresa
    projetos = [
        # nome / numero / local / priority (1-5) / department
        "Salao De Festas, 001, 3 andar, 5, Eventos\n",
        "Predio Novo, 002, 4 andar, 3, Construção\n",
        "Reformas, 003, 5 andar, 2, Manutenção\n"
    ]
    
    # Abre o arquivo de texto para escrita
    with open(arquivo_nome, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(projetos)
    
    print(f'Banco de dados {arquivo_nome} criado com sucesso!')

# Criar o banco de dados em formato texto
add_project('firm.txt')

# Função para adicionar informações a um banco de dados simples em um arquivo de texto
def update_project(arquivo_nome, name, number, local, priority, department):
    # Dados a serem adicionados
    new_info = f"{name}, {number}, {local}, {priority}, {department}\n"
    
    # Abre o arquivo em modo de acréscimo ('a') para adicionar novas informações
    with open(arquivo_nome, 'a', encoding='utf-8') as arquivo:
        arquivo.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_project('firm.txt',"Inovacao", "004", "5 andar", "5", "Pesquisa")

# Função para exibir os projetos
def show_project(arquivo_nome):
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # Dividindo a linha em partes e formatando a exibição
                name, number, local, priority, department = linha.strip().split(', ')
                print(f'Nome: {name}, Numero: {number}, Local: {local}, Priority: {priority}, Department: {department}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_nome} não foi encontrado.')

# Exibir os projetos
show_project('firm.txt')
