# Função para criar um banco de dados simples em um arquive de texto
def add_project(arquive_name):
    # Dados Empresa 
    project = [
        # nome/ numero/ local
        "Salao De Festas, 001, 3 andar\n",
        "Predio Novo, 002, 4 andar\n",
        "Reformas, 003, 5 andar\n"
    ]
    
    # Abre o arquive de texto para escrita
    with open(arquive_name, 'w', encoding='utf-8') as arquive:
        arquive.writelines(project)
    
    print(f'Banco de dados {arquive_name} criado com sucesso!')

# Criar o banco de dados em formato texto
add_project('department.txt')

# Função para adicionar informações a um banco de dados simples em um arquive de texto
def update_project(arquive_name, name, number, local):
    # Dados a serem adicionados
    new_info = f"{name}, {number}, {local}\n"
    
    # Abre o arquive em modo de acréscimo ('a') para adicionar novas informações
    with open(arquive_name, 'a', encoding='utf-8') as arquive:
        arquive.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_project('department.txt',"Inovacao", "004", "5 andar")

def show_project(arquive_name):
    try:
        with open(arquive_name, 'r', encoding='utf-8') as arquive:
            lines = arquive.readlines()
            for line in lines:
                # Dividindo a linha em partes e formatando a exibição
                name, number, local = line.strip().split(', ')
                print(f'Nome: {name}, Numero: {number}, Local: {local}')
    except FileNotFoundError:
        print(f'O arquivo {arquive_name} não foi encontrado.')

show_project('department.txt')
