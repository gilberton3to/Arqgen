from PyQt5 import uic, QtWidgets
import sys
from databaseconnect import hostname, database, username, pwd, port_id
import psycopg2
import psycopg2.extras

# Função para conectar ao banco de dados
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id
        )
        return conn
    except Exception as error:
        print("Erro ao conectar ao banco de dados:", error)
        return None

############################################# FUNCIONÁRIOS

# Função para preencher a tabela de funcionários com os dados do banco de dados
def preencher_tabela_funcionarios():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM employee")
                funcionarios = cur.fetchall()

                employees.tabelafuncionarios.setRowCount(0)  # Limpa a tabela
                for funcionario in funcionarios:
                    row_position = employees.tabelafuncionarios.rowCount()
                    employees.tabelafuncionarios.insertRow(row_position)
                    employees.tabelafuncionarios.setItem(row_position, 0, QtWidgets.QTableWidgetItem(funcionario['name']))
                    employees.tabelafuncionarios.setItem(row_position, 1, QtWidgets.QTableWidgetItem(funcionario['cpf']))
                    employees.tabelafuncionarios.setItem(row_position, 2, QtWidgets.QTableWidgetItem(funcionario['role']))
                    employees.tabelafuncionarios.setItem(row_position, 3, QtWidgets.QTableWidgetItem(funcionario['address']))
                    employees.tabelafuncionarios.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(funcionario['salary'])))
                    employees.tabelafuncionarios.setItem(row_position, 5, QtWidgets.QTableWidgetItem(funcionario['gender']))
                    employees.tabelafuncionarios.setItem(row_position, 6, QtWidgets.QTableWidgetItem(str(funcionario['birth_date'])))
                    employees.tabelafuncionarios.setItem(row_position, 7, QtWidgets.QTableWidgetItem(funcionario['education']))
                    employees.tabelafuncionarios.setItem(row_position, 8, QtWidgets.QTableWidgetItem(str(funcionario['department_id'])))
        except Exception as error:
            print("Erro ao buscar funcionários:", error)
        finally:
            conn.close()

# Função para adicionar ou atualizar funcionários no banco de dados
def salvar_dados_funcionarios():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cur:
                for row in range(employees.tabelafuncionarios.rowCount()):
                    name = employees.tabelafuncionarios.item(row, 0).text()
                    cpf = employees.tabelafuncionarios.item(row, 1).text()
                    role = employees.tabelafuncionarios.item(row, 2).text()
                    address = employees.tabelafuncionarios.item(row, 3).text()
                    salary = int(employees.tabelafuncionarios.item(row, 4).text())
                    gender = employees.tabelafuncionarios.item(row, 5).text()
                    birth_date = employees.tabelafuncionarios.item(row, 6).text()
                    education = employees.tabelafuncionarios.item(row, 7).text()
                    department_id = int(employees.tabelafuncionarios.item(row, 8).text())

                    cur.execute('''
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
                    ''', (name, cpf, role, address, salary, gender, birth_date, education, department_id))
                conn.commit()
                print("Dados dos funcionários salvos no banco de dados.")
        except Exception as error:
            print("Erro ao salvar funcionários:", error)
        finally:
            conn.close()
    preencher_tabela_funcionarios()  # Atualiza a tabela após salvar

# Função para remover um funcionário do banco de dados
def remover_funcionario():
    row = employees.tabelafuncionarios.currentRow()
    if row >= 0:
        cpf = employees.tabelafuncionarios.item(row, 1).text()
        conn = connect_db()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM employee WHERE cpf = %s", (cpf,))
                    conn.commit()
                    print("Funcionário removido do banco de dados.")
            except Exception as error:
                print("Erro ao remover funcionário:", error)
            finally:
                conn.close()
        employees.tabelafuncionarios.removeRow(row)
    else:
        print("Nenhuma linha selecionada para remover.")

############################################# DEPARTAMENTOS

# Função para preencher a tabela de departamentos com os dados do banco de dados
def preencher_tabela_departamentos():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM department")
                departamentos = cur.fetchall()

                departaments.tabeladepartamentos.setRowCount(0)  # Limpa a tabela
                for departamento in departamentos:
                    row_position = departaments.tabeladepartamentos.rowCount()
                    departaments.tabeladepartamentos.insertRow(row_position)
                    departaments.tabeladepartamentos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(departamento['number'])))
                    departaments.tabeladepartamentos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(departamento['name']))
                    departaments.tabeladepartamentos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(departamento['manager']))
                    departaments.tabeladepartamentos.setItem(row_position, 3, QtWidgets.QTableWidgetItem(departamento['headquarters']))
        except Exception as error:
            print("Erro ao buscar departamentos:", error)
        finally:
            conn.close()

# Função para adicionar ou atualizar departamentos no banco de dados
def salvar_dados_departamentos():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cur:
                for row in range(departaments.tabeladepartamentos.rowCount()):
                    number = int(departaments.tabeladepartamentos.item(row, 0).text())
                    name = departaments.tabeladepartamentos.item(row, 1).text()
                    manager = departaments.tabeladepartamentos.item(row, 2).text()
                    headquarters = departaments.tabeladepartamentos.item(row, 3).text()

                    cur.execute('''
                        INSERT INTO department (number, name, manager, headquarters)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (number) DO UPDATE SET
                            name = EXCLUDED.name,
                            manager = EXCLUDED.manager,
                            headquarters = EXCLUDED.headquarters
                    ''', (number, name, manager, headquarters))
                conn.commit()
                print("Dados dos departamentos salvos no banco de dados.")
        except Exception as error:
            print("Erro ao salvar departamentos:", error)
        finally:
            conn.close()
    preencher_tabela_departamentos()  # Atualiza a tabela após salvar

# Função para remover um departamento do banco de dados
def remover_departamento():
    row = departaments.tabeladepartamentos.currentRow()
    if row >= 0:
        number = departaments.tabeladepartamentos.item(row, 0).text()
        conn = connect_db()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM department WHERE number = %s", (number,))
                    conn.commit()
                    print("Departamento removido do banco de dados.")
            except Exception as error:
                print("Erro ao remover departamento:", error)
            finally:
                conn.close()
        departaments.tabeladepartamentos.removeRow(row)
    else:
        print("Nenhuma linha selecionada para remover.")

############################################# PROJETOS

# Função para preencher a tabela de projetos com os dados do banco de dados
def preencher_tabela_projetos():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM firm")
                projetos = cur.fetchall()

                projects.tabelaprojetos.setRowCount(0)  # Limpa a tabela
                for projeto in projetos:
                    row_position = projects.tabelaprojetos.rowCount()
                    projects.tabelaprojetos.insertRow(row_position)
                    projects.tabelaprojetos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(projeto['code'])))
                    projects.tabelaprojetos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(projeto['name']))
                    projects.tabelaprojetos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(projeto['location']))
                    projects.tabelaprojetos.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(projeto['priority'])))
                    projects.tabelaprojetos.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(projeto['department_id'])))
        except Exception as error:
            print("Erro ao buscar projetos:", error)
        finally:
            conn.close()

# Função para adicionar ou atualizar projetos no banco de dados
def salvar_dados_projetos():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cur:
                for row in range(projects.tabelaprojetos.rowCount()):
                    code = int(projects.tabelaprojetos.item(row, 0).text())
                    name = projects.tabelaprojetos.item(row, 1).text()
                    location = projects.tabelaprojetos.item(row, 2).text()
                    priority = int(projects.tabelaprojetos.item(row, 3).text())
                    department_id = int(projects.tabelaprojetos.item(row, 4).text())

                    cur.execute('''
                        INSERT INTO firm (code, name, location, priority, department_id)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (code) DO UPDATE SET
                            name = EXCLUDED.name,
                            location = EXCLUDED.location,
                            priority = EXCLUDED.priority,
                            department_id = EXCLUDED.department_id
                    ''', (code, name, location, priority, department_id))
                conn.commit()
                print("Dados dos projetos salvos no banco de dados.")
        except Exception as error:
            print("Erro ao salvar projetos:", error)
        finally:
            conn.close()
    preencher_tabela_projetos()  # Atualiza a tabela após salvar

# Função para remover um projeto do banco de dados
def remover_projeto():
    row = projects.tabelaprojetos.currentRow()
    if row >= 0:
        code = projects.tabelaprojetos.item(row, 0).text()
        conn = connect_db()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM firm WHERE code = %s", (code,))
                    conn.commit()
                    print("Projeto removido do banco de dados.")
            except Exception as error:
                print("Erro ao remover projeto:", error)
            finally:
                conn.close()
        projects.tabelaprojetos.removeRow(row)
    else:
        print("Nenhuma linha selecionada para remover.")




############################################# FUNCIONÁRIOS

# Função para carregar dados da linha selecionada para edição
def editar_funcionarios():
    row = employees.tabelafuncionarios.currentRow()
    if row >= 0:
        employees.nome.setText(employees.tabelafuncionarios.item(row, 0).text())
        employees.cpf.setText(employees.tabelafuncionarios.item(row, 1).text())
        employees.cargo.setText(employees.tabelafuncionarios.item(row, 2).text())
        employees.endereco.setText(employees.tabelafuncionarios.item(row, 3).text())
        employees.salario.setText(employees.tabelafuncionarios.item(row, 4).text())
        employees.genero.setText(employees.tabelafuncionarios.item(row, 5).text())
        employees.nascimento.setText(employees.tabelafuncionarios.item(row, 6).text())
        employees.formacao.setText(employees.tabelafuncionarios.item(row, 7).text())
        employees.departamento.setText(employees.tabelafuncionarios.item(row, 8).text())
    else:
        print("Nenhuma linha selecionada para edição.")

# Função para salvar os dados da tabela no arquivo
def salvar_dados_funcionarios():
    with open('workers.txt', 'w', encoding='utf-8') as file:
        for row in range(employees.tabelafuncionarios.rowCount()):
            name = employees.tabelafuncionarios.item(row, 0).text()
            cpf = employees.tabelafuncionarios.item(row, 1).text()
            cargo = employees.tabelafuncionarios.item(row, 2).text()
            address = employees.tabelafuncionarios.item(row, 3).text()
            salary = employees.tabelafuncionarios.item(row, 4).text()
            gender = employees.tabelafuncionarios.item(row, 5).text()
            birth = employees.tabelafuncionarios.item(row, 6).text()
            formation = employees.tabelafuncionarios.item(row, 7).text()
            department = employees.tabelafuncionarios.item(row, 8).text()
            file.write(f"{name}, {cpf}, {cargo}, {address}, {salary}, {gender}, {birth}, {formation}, {department}\n")
    print("Dados salvos com sucesso no arquivo workers.txt.")
    employees.adicionar.clicked.connect(adicionar_nova_linha_funcionario)
    preencher_tabela_funcionarios()  # Atualiza a tabela após salvar

# Função para atualizar a tabela com os dados editados
def atualizar_funcionarios():
    row = employees.tabelafuncionarios.currentRow()
    if row >= 0:
        employees.tabelafuncionarios.setItem(row, 0, QtWidgets.QTableWidgetItem(employees.nome.text()))
        employees.tabelafuncionarios.setItem(row, 1, QtWidgets.QTableWidgetItem(employees.cpf.text()))
        employees.tabelafuncionarios.setItem(row, 2, QtWidgets.QTableWidgetItem(employees.cargo.text()))
        employees.tabelafuncionarios.setItem(row, 3, QtWidgets.QTableWidgetItem(employees.endereco.text()))
        employees.tabelafuncionarios.setItem(row, 4, QtWidgets.QTableWidgetItem(employees.salario.text()))
        employees.tabelafuncionarios.setItem(row, 5, QtWidgets.QTableWidgetItem(employees.genero.text()))
        employees.tabelafuncionarios.setItem(row, 6, QtWidgets.QTableWidgetItem(employees.nascimento.text()))
        employees.tabelafuncionarios.setItem(row, 7, QtWidgets.QTableWidgetItem(employees.formacao.text()))
        employees.tabelafuncionarios.setItem(row, 8, QtWidgets.QTableWidgetItem(employees.departamento.text()))
    else:
        print("Nenhuma linha selecionada para atualizar.")
        
############################################# DEPARTAMENTOS

# Função para carregar dados da linha selecionada para edição
def editar_departamentos():
    row = departaments.tabeladepartamentos.currentRow()
    if row >= 0:
        departaments.numero.setText(departaments.tabeladepartamentos.item(row, 0).text())
        departaments.nome.setText(departaments.tabeladepartamentos.item(row, 1).text())
        departaments.gerente.setText(departaments.tabeladepartamentos.item(row, 2).text())
        departaments.sede.setText(departaments.tabeladepartamentos.item(row, 3).text())
    else:
        print("Nenhuma linha selecionada para edição.")

# Função para salvar os dados da tabela no arquivo
def salvar_dados_departamentos():
    with open('department.txt', 'w', encoding='utf-8') as file:
        for row in range(departaments.tabeladepartamentos.rowCount()):
            number = departaments.tabeladepartamentos.item(row, 0).text()
            name = departaments.tabeladepartamentos.item(row, 1).text()
            manager = departaments.tabeladepartamentos.item(row, 2).text()
            headquarter = departaments.tabeladepartamentos.item(row, 3).text()
            file.write(f"{number}, {name}, {manager}, {headquarter}\n")
    print("Dados salvos com sucesso no arquivo department.txt.")
    departaments.adicionar.clicked.connect(adicionar_nova_linha_departamento)
    preencher_tabela_departamentos()  # Atualiza a tabela após salvar

# Função para atualizar a tabela com os dados editados
def atualizar_departamentos():
    row = departaments.tabeladepartamentos.currentRow()
    if row >= 0:
        departaments.tabeladepartamentos.setItem(row, 0, QtWidgets.QTableWidgetItem(departaments.numero.text()))
        departaments.tabeladepartamentos.setItem(row, 1, QtWidgets.QTableWidgetItem(departaments.nome.text()))
        departaments.tabeladepartamentos.setItem(row, 2, QtWidgets.QTableWidgetItem(departaments.gerente.text()))
        departaments.tabeladepartamentos.setItem(row, 3, QtWidgets.QTableWidgetItem(departaments.sede.text()))
    else:
        print("Nenhuma linha selecionada para atualizar.")

############################################# PROJETOS

# Função para carregar dados da linha selecionada para edição
def editar_projetos():
    row = projects.tabelaprojetos.currentRow()
    if row >= 0:
        projects.codigo.setText(projects.tabelaprojetos.item(row, 0).text())
        projects.nome.setText(projects.tabelaprojetos.item(row, 1).text())
        projects.local.setText(projects.tabelaprojetos.item(row, 2).text())
        projects.prioridade.setText(projects.tabelaprojetos.item(row, 3).text())
        projects.departamento.setText(projects.tabelaprojetos.item(row, 4).text())
    else:
        print("Nenhuma linha selecionada para edição.")

# Função para salvar os dados da tabela no arquivo
def salvar_dados_projetos():
    with open('firm.txt', 'w', encoding='utf-8') as file:
        for row in range(projects.tabelaprojetos.rowCount()):
            code = projects.tabelaprojetos.item(row, 0).text()
            name = projects.tabelaprojetos.item(row, 1).text()
            local = projects.tabelaprojetos.item(row, 2).text()
            priority = projects.tabelaprojetos.item(row, 3).text()
            department = projects.tabelaprojetos.item(row, 4).text()
            file.write(f"{code}, {name}, {local}, {priority}, {department}\n")
    print("Dados salvos com sucesso no arquivo firm.txt.")
    projects.adicionar.clicked.connect(adicionar_nova_linha_projeto)
    preencher_tabela_projetos()  # Atualiza a tabela após salvar

# Função para atualizar a tabela com os dados editados
def atualizar_projetos():
    row = projects.tabeladepartamentos.currentRow()
    if row >= 0:
        projects.tabelaprojetos.setItem(row, 0, QtWidgets.QTableWidgetItem(projects.codigo.text()))
        projects.tabelaprojetos.setItem(row, 1, QtWidgets.QTableWidgetItem(projects.nome.text()))
        projects.tabelaprojetos.setItem(row, 2, QtWidgets.QTableWidgetItem(projects.local.text()))
        projects.tabelaprojetos.setItem(row, 3, QtWidgets.QTableWidgetItem(projects.prioridade.text()))
        projects.tabelaprojetos.setItem(row, 4, QtWidgets.QTableWidgetItem(projects.departamento.text()))
    else:
        print("Nenhuma linha selecionada para atualizar.")
        


#############################################

# Funções de logout para fechar as janelas
def logout1():
    general.close()

def logout2():
    employees.close()

def logout3():
    departaments.close()

def logout4():
    projects.close()

# Funções para chamar telas e preencher as tabelas
def chamar_tela_homeview():
    home.show()

def chamar_tela_generalview():
    general.show()

def chamar_tela_employeesview():
    preencher_tabela_funcionarios()  # Preenche a tabela antes de mostrar a tela
    employees.show()

def chamar_tela_departamentsview():
    preencher_tabela_departamentos()  # Preenche a tabela antes de mostrar a tela
    departaments.show()

def chamar_tela_projectsview():
    preencher_tabela_projetos()  # Preenche a tabela antes de mostrar a tela
    projects.show()
    
######################################

def adicionar_nova_linha_funcionario():
    row_position = employees.tabelafuncionarios.rowCount()
    employees.tabelafuncionarios.insertRow(row_position)
    
def remover_funcionario():
    row = employees.tabelafuncionarios.currentRow()
    if row >= 0:
        employees.tabelafuncionarios.removeRow(row)
        print("Funcionário removido.")
    else:
        print("Nenhuma linha selecionada para remover.")

######################################

def adicionar_nova_linha_departamento():
    row_position = departaments.tabeladepartamentos.rowCount()
    departaments.tabeladepartamentos.insertRow(row_position)
    
def remover_departamento():
    row = departaments.tabeladepartamentos.currentRow()
    if row >= 0:
        departaments.tabeladepartamentos.removeRow(row)
        print("Departamento removido.")
    else:
        print("Nenhuma linha selecionada para remover.")
        
######################################
        
def adicionar_nova_linha_projeto():
    row_position = projects.tabelaprojetos.rowCount()
    projects.tabelaprojetos.insertRow(row_position)
    
def remover_projeto():
    row = projects.tabelaprojetos.currentRow()
    if row >= 0:
        projects.tabelaprojetos.removeRow(row)
        print("Projeto removido.")
    else:
        print("Nenhuma linha selecionada para remover.")
        
######################################

app = QtWidgets.QApplication(sys.argv)

# Carrega as telas
home = uic.loadUi("screens/HomeView.ui")
general = uic.loadUi("screens/GeneralView.ui")
employees = uic.loadUi("screens/EmployeesView.ui")
departaments = uic.loadUi("screens/DepartamentsView.ui")
projects = uic.loadUi("screens/ProjectsView.ui")

# Conecta os botões para navegar entre as telas
home.entrar.clicked.connect(chamar_tela_generalview)
general.parafuncionarios.clicked.connect(chamar_tela_employeesview)
general.paradepartamentos.clicked.connect(chamar_tela_departamentsview)
general.paraprojetos.clicked.connect(chamar_tela_projectsview)

# Conecta os botões de logout para fechar as telas
general.sair.clicked.connect(logout1)
employees.sair.clicked.connect(logout2)
departaments.sair.clicked.connect(logout3)
projects.sair.clicked.connect(logout4)

# Conecta os botões de edição e salvar
employees.editar.clicked.connect(editar_funcionarios)
employees.salvar.clicked.connect(salvar_dados_funcionarios)
employees.atualizar.clicked.connect(atualizar_funcionarios)
employees.adicionar.clicked.connect(adicionar_nova_linha_funcionario)
employees.apagar.clicked.connect(remover_funcionario)

departaments.editar.clicked.connect(editar_departamentos)
departaments.salvar.clicked.connect(salvar_dados_departamentos)
departaments.atualizar.clicked.connect(atualizar_departamentos)
departaments.adicionar.clicked.connect(adicionar_nova_linha_departamento)
departaments.apagar.clicked.connect(remover_departamento)

projects.editar.clicked.connect(editar_projetos)
projects.salvar.clicked.connect(salvar_dados_projetos)
projects.atualizar.clicked.connect(atualizar_projetos)
projects.adicionar.clicked.connect(adicionar_nova_linha_projeto)
projects.apagar.clicked.connect(remover_projeto)

# Inicia a aplicação
home.show()
sys.exit(app.exec())