import psycopg2
import psycopg2.extras

# Configuração do banco de dados
hostname = "localhost"
database = "arqgen"
username = "postgres"
pwd = "g212002"
port_id = 5432

# Função para criar a tabela de projetos (firm) se não existir
def create_project_table():
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor() as cur:
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS firm (
                    id SERIAL PRIMARY KEY,
                    number INT UNIQUE NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    location VARCHAR(100),
                    priority INT CHECK (priority BETWEEN 1 AND 5),
                    department VARCHAR(50)
                )
                '''
                cur.execute(create_table_query)
                conn.commit()
                print("Tabela 'firm' criada com sucesso!")

    except Exception as error:
        print("Erro ao criar tabela:", error)

# Função para adicionar ou atualizar projetos no banco de dados
def add_project(number, name, location, priority, department):
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor() as cur:
                insert_query = '''
                INSERT INTO firm (number, name, location, priority, department)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (number) DO UPDATE SET
                    name = EXCLUDED.name,
                    location = EXCLUDED.location,
                    priority = EXCLUDED.priority,
                    department = EXCLUDED.department
                '''
                cur.execute(insert_query, (number, name, location, priority, department))
                conn.commit()
                print(f'Projeto {name} adicionado ou atualizado com sucesso!')

    except Exception as error:
        print("Erro ao adicionar projeto:", error)

# Função para exibir os projetos cadastrados
def show_project():
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM firm")
                projetos = cur.fetchall()

                if not projetos:
                    print("Nenhum projeto cadastrado.")
                else:
                    for projeto in projetos:
                        print(f"Nome: {projeto['name']}, Numero: {projeto['number']}, "
                              f"Local: {projeto['location']}, Prioridade: {projeto['priority']}, "
                              f"Departamento: {projeto['department']}")

    except Exception as error:
        print("Erro ao buscar projetos:", error)


# Criar a tabela se ainda não existir
create_project_table()

# Adicionar projetos de exemplo
add_project(1, "Salão De Festas", "3º andar", 5, "Eventos")
add_project(2, "Prédio Novo", "4º andar", 3, "Construção")
add_project(3, "Reformas", "5º andar", 2, "Manutenção")
add_project(4, "Inovação", "5º andar", 5, "Pesquisa")

# Mostrar os projetos cadastrados
show_project()
