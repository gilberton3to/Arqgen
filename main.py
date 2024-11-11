from PyQt5 import uic, QtWidgets
import sys

# Função para preencher a tabela de funcionários com os dados do arquivo
def preencher_tabela_funcionarios():
    employees.tabelafuncionarios.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
    employees.tabelafuncionarios.setRowCount(0)  # Limpa a tabela antes de adicionar novas linhas
    try:
        with open('workers.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, cpf, position, address, salary, gender, birth = line.strip().split(', ')
                row_position = employees.tabelafuncionarios.rowCount()
                employees.tabelafuncionarios.insertRow(row_position)
                employees.tabelafuncionarios.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name))
                employees.tabelafuncionarios.setItem(row_position, 1, QtWidgets.QTableWidgetItem(cpf))
                employees.tabelafuncionarios.setItem(row_position, 2, QtWidgets.QTableWidgetItem(position))
                employees.tabelafuncionarios.setItem(row_position, 3, QtWidgets.QTableWidgetItem(address))
                employees.tabelafuncionarios.setItem(row_position, 4, QtWidgets.QTableWidgetItem(salary))
                employees.tabelafuncionarios.setItem(row_position, 5, QtWidgets.QTableWidgetItem(gender))
                employees.tabelafuncionarios.setItem(row_position, 6, QtWidgets.QTableWidgetItem(birth))
    except FileNotFoundError:
        print("Arquivo workers.txt não encontrado.")

# Função para preencher a tabela de departamentos com os dados do arquivo
def preencher_tabela_departamentos():
    departaments.tabeladepartamentos.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
    departaments.tabeladepartamentos.setRowCount(0)
    try:
        with open('department.txt', 'r', encoding='utf-8') as file:
            for line in file:
                number, name, manager = line.strip().split(', ')
                row_position = departaments.tabeladepartamentos.rowCount()
                departaments.tabeladepartamentos.insertRow(row_position)
                departaments.tabeladepartamentos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(number))
                departaments.tabeladepartamentos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(name))
                departaments.tabeladepartamentos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(manager))
    except FileNotFoundError:
        print("Arquivo department.txt não encontrado.")

# Função para preencher a tabela de projetos com os dados do arquivo
def preencher_tabela_projetos():
    projects.tabelaprojetos.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
    projects.tabelaprojetos.setRowCount(0)
    try:
        with open('firm.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, number, local = line.strip().split(', ')
                row_position = projects.tabelaprojetos.rowCount()
                projects.tabelaprojetos.insertRow(row_position)
                projects.tabelaprojetos.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name))
                projects.tabelaprojetos.setItem(row_position, 1, QtWidgets.QTableWidgetItem(number))
                projects.tabelaprojetos.setItem(row_position, 2, QtWidgets.QTableWidgetItem(local))
    except FileNotFoundError:
        print("Arquivo firm.txt não encontrado.")

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
            file.write(f"{name}, {cpf}, {cargo}, {address}, {salary}, {gender}, {birth}\n")
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
    else:
        print("Nenhuma linha selecionada para edição.")

# Função para salvar os dados da tabela no arquivo
def salvar_dados_departamentos():
    with open('department.txt', 'w', encoding='utf-8') as file:
        for row in range(departaments.tabeladepartamentos.rowCount()):
            number = departaments.tabeladepartamentos.item(row, 0).text()
            name = departaments.tabeladepartamentos.item(row, 1).text()
            manager = departaments.tabeladepartamentos.item(row, 2).text()
            file.write(f"{number}, {name}, {manager}\n")
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
    else:
        print("Nenhuma linha selecionada para edição.")

# Função para salvar os dados da tabela no arquivo
def salvar_dados_projetos():
    with open('firm.txt', 'w', encoding='utf-8') as file:
        for row in range(projects.tabelaprojetos.rowCount()):
            code = projects.tabelaprojetos.item(row, 0).text()
            name = projects.tabelaprojetos.item(row, 1).text()
            local = projects.tabelaprojetos.item(row, 2).text()
            file.write(f"{code}, {name}, {local}\n")
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
