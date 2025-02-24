import psycopg2
import psycopg2.extras

# Configuração do banco de dados
hostname = "localhost"
database = "arqgen"
username = "postgres"
pwd = "g212002"
port_id = 5432

conn = None

try:
    with psycopg2.connect(
        dbname=database,
        user=username,
        password=pwd,
        host=hostname,
        port=port_id) as conn:
    
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            
            # Remover tabelas se existirem para recriação
            cur.execute("DROP TABLE IF EXISTS employee, firm, department CASCADE")

            # Criar tabela department
            create_department = '''
            CREATE TABLE IF NOT EXISTS department (
                id SERIAL PRIMARY KEY,
                number INT UNIQUE NOT NULL,
                name VARCHAR(50) NOT NULL,
                manager VARCHAR(40),
                headquarters VARCHAR(100)
            )
            '''
            cur.execute(create_department)

            # Criar tabela firm (projetos)
            create_firm = '''
            CREATE TABLE IF NOT EXISTS firm (
                id SERIAL PRIMARY KEY,
                code INT UNIQUE NOT NULL,
                name VARCHAR(50) NOT NULL,
                location VARCHAR(100),
                priority INT,
                department_id INT REFERENCES department(id) ON DELETE SET NULL
            )
            '''
            cur.execute(create_firm)

            # Criar tabela employee
            create_employee = ''' 
            CREATE TABLE IF NOT EXISTS employee (
                id SERIAL PRIMARY KEY,        
                name VARCHAR(40) NOT NULL,    
                cpf VARCHAR(14) UNIQUE NOT NULL,     
                role VARCHAR(50),             
                address TEXT,                 
                salary INT,                   
                gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),  
                birth_date DATE,              
                education VARCHAR(100),       
                department_id INT REFERENCES department(id) ON DELETE SET NULL
            ) 
            '''
            cur.execute(create_employee)

            # Inserir departamentos
            insert_department = '''
            INSERT INTO department (number, name, manager, headquarters)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (number) DO UPDATE SET
                name = EXCLUDED.name,
                manager = EXCLUDED.manager,
                headquarters = EXCLUDED.headquarters
            RETURNING id
            '''
            
            department_values = [
                (101, 'TI', 'Carlos Silva', 'São Paulo'),
                (102, 'MKT', 'Ana Souza', 'Rio de Janeiro')
            ]
            
            cur.executemany(insert_department, department_values)
            conn.commit()  # Confirma para permitir referências
            
            # Recuperar IDs dos departamentos
            cur.execute("SELECT number, id FROM department")
            department_map = {row['number']: row['id'] for row in cur.fetchall()}

            # Inserir projetos (firm)
            insert_firm = '''
            INSERT INTO firm (code, name, location, priority, department_id)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (code) DO UPDATE SET
                name = EXCLUDED.name,
                location = EXCLUDED.location,
                priority = EXCLUDED.priority,
                department_id = EXCLUDED.department_id
            '''
            
            firm_values = [
                (1, 'Projeto Apollo', 'São Paulo', 1, department_map[101]),
                (2, 'Expansão Digital', 'Rio de Janeiro', 2, department_map[102])
            ]
            
            cur.executemany(insert_firm, firm_values)

            # Inserir funcionários
            insert_employee = '''
            INSERT INTO employee (name, cpf, role, address, salary, gender, birth_date, education, department_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (cpf) DO UPDATE SET 
                name = EXCLUDED.name,
                role = EXCLUDED.role,
                address = EXCLUDED.address,
                salary = EXCLUDED.salary,
                gender = EXCLUDED.gender,
                birth_date = EXCLUDED.birth_date,
                education = EXCLUDED.education,
                department_id = EXCLUDED.department_id
            '''
            
            employee_values = [
                ('Gilberto Neto', '123.456.789-00', 'Engenheiro de Software', 'Rua das Inovações, 123', 8500, 'M', '1998-05-15', 'Engenharia de Computação', department_map[101]),
                ('Leo Cavalcante', '124.256.089-01', 'Designer', 'Porco Anélio, 321', 1900, 'M', '2002-09-16', 'Design', department_map[102])
            ]
            
            cur.executemany(insert_employee, employee_values)

            # Atualizar salário
            update_salary = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_salary)
            
            # Excluir um funcionário específico
            delete_employee = 'DELETE FROM employee WHERE name = %s'
            cur.execute(delete_employee, ('Leo Cavalcante',))

            # Buscar e exibir os funcionários restantes
            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall():
                print(record['name'], record['salary'])
            
            # Salvar as alterações
            conn.commit()

except Exception as error:
    print("Erro:", error)

finally:
    if conn is not None:
        conn.close()