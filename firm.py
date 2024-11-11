# Função para criar um banco de dados simples em um arquive de texto
def add_department(arquive_name):
    # Dados Empresa 
    departments = [
        # Controle de departamentos: nome/ number/ gerente
        "Contabilidade, 008, João\n",
        "Gestão, 001, Maria\n",
        "Recursos Humanos, 004, Pedro\n"
    ]
    
    # Abre o arquive de texto para escrita
    with open(arquive_name, 'w', encoding='utf-8') as arquive:
        arquive.writelines(departments)
    
    print(f'Banco de dados {arquive_name} criado com sucesso!')

# Criar o banco de dados em formato texto
add_department('firm.txt')

# Função para adicionar informações a um banco de dados simples em um arquive de texto
def update_department(arquive_name, name, number, manager):
    # Dados a serem adicionados
    new_info = f"{name}, {number}, {manager}\n"
    
    # Abre o arquive em modo de acréscimo ('a') para adicionar novas informações
    with open(arquive_name, 'a', encoding='utf-8') as arquive:
        arquive.write(new_info)
    
    print(f'Informações de {name} adicionadas ao banco de dados com sucesso!')

# Exemplo de uso
update_department('firm.txt',"Desenvolvimento", "012", 'Ana')

def show_department(arquive_name):
    try:
        with open(arquive_name, 'r', encoding='utf-8') as arquive:
            lines = arquive.readlines()
            for line in lines:
                # Dividindo a linha em partes e formatando a exibição
                name, number, manager = line.strip().split(', ')
                print(f'Nome: {name}, Numero: {number}, Gerente: {manager}')
    except FileNotFoundError:
        print(f'O arquivo {arquive_name} não foi encontrado.')

show_department('firm.txt')
