import psycopg2
import psycopg2.extras

# Configuração do banco de dados
hostname = "localhost"
database = "arqgen"
username = "postgres"
pwd = "g212002"
port_id = 5432

# Função para criar a tabela de funcionários (workers) se não existir
def create_worker_table():
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor() as cur:
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS workers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    cpf VARCHAR(14) UNIQUE NOT NULL,
                    position VARCHAR(50) NOT NULL,
                    address VARCHAR(150),
                    salary DECIMAL(10,2) CHECK (salary >= 0),
                    gender CHAR(1) CHECK (gender IN ('M', 'F')),
                    birth DATE NOT NULL,
                    formation VARCHAR(50),
                    department_id INT REFERENCES department(id) ON DELETE SET NULL
                )
                '''
                cur.execute(create_table_query)
                conn.commit()
                print("Tabela 'workers' criada com sucesso!")

    except Exception as error:
        print("Erro ao criar tabela:", error)

# Função para adicionar ou atualizar funcionários no banco de dados
def add_worker(name, cpf, position, address, salary, gender, birth, formation, department_id):
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor() as cur:
                insert_query = '''
                INSERT INTO workers (name, cpf, position, address, salary, gender, birth, formation, department_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (cpf) DO UPDATE SET
                    name = EXCLUDED.name,
                    position = EXCLUDED.position,
                    address = EXCLUDED.address,
                    salary = EXCLUDED.salary,
                    gender = EXCLUDED.gender,
                    birth = EXCLUDED.birth,
                    formation = EXCLUDED.formation,
                    department_id = EXCLUDED.department_id
                '''
                cur.execute(insert_query, (name, cpf, position, address, salary, gender, birth, formation, department_id))
                conn.commit()
                print(f'Funcionário {name} adicionado ou atualizado com sucesso!')

    except Exception as error:
        print("Erro ao adicionar funcionário:", error)

# Função para exibir os funcionários cadastrados
def show_workers():
    try:
        with psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM workers")
                funcionarios = cur.fetchall()

                if not funcionarios:
                    print("Nenhum funcionário cadastrado.")
                else:
                    for funcionario in funcionarios:
                        print(f"Nome: {funcionario['name']}, CPF: {funcionario['cpf']}, Cargo: {funcionario['position']}, "
                              f"Endereço: {funcionario['address']}, Salário: {funcionario['salary']}, "
                              f"Gênero: {funcionario['gender']}, Nascimento: {funcionario['birth']}, "
                              f"Formação: {funcionario['formation']}, Departamento ID: {funcionario['department_id']}")

    except Exception as error:
        print("Erro ao buscar funcionários:", error)


# Criar a tabela se ainda não existir
create_worker_table()

# Adicionar funcionários de exemplo
add_worker("João", "324.345.678-89", "Gerente", "Rua D", 8000.00, "M", "1979-03-09", "Superior", 1)
add_worker("Maria", "234.765.356-98", "Analista", "Rua Felizberto", 12000.00, "F", "2003-12-23", "Superior incompleto", 2)
add_worker("Pedro", "924.275.634-73", "Supervisor", "Rua Felizberto", 9000.00, "M", "2003-12-23", "Superior", 3)
add_worker("Ana", "765.234.356-98", "Gerente", "Rua Farias", 14000.00, "F", "2003-12-23", "Superior", 1)

# Mostrar os funcionários cadastrados
show_workers()