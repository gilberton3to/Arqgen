from PyQt5 import uic, QtWidgets, QtCore

#FUNCOES LOGOUT
def logout1():
    general.close()

def logout2():
    employees.close()

def logout3():
    departaments.close()

def logout4():
    projects.close()

#FUNCOES CHAMAR TELA

def chamar_tela_homeview():
    home.show()

def chamar_tela_generalview():
    general.show()

def chamar_tela_employeesview():
    # row = employees.tabelafuncionarios.currentRow()
    # nome = employees.tabelafuncionarios.item(row, 0).text()
    # cpf = employees.tabelafuncionarios.item(row, 1).text()
    # cargo = employees.tabelafuncionarios.item(row, 2).text()
    # end = employees.tabelafuncionarios.item(row, 3).text()
    # sal = employees.tabelafuncionarios.item(row, 4).text()
    
    # employees.funcionarios_nome.setPlaceholderText(nome)
    # employees.funcionarios_cpf.setPlaceholderText(cpf)
    # employees.funcionarios_cargo.setPlaceholderText(cargo)
    # employees.funcionarios_end.setPlaceholderText(end)
    # employees.funcionarios_sal.setPlaceholderText(sal)

    employees.close()
    employees.show()

def chamar_tela_departamentsview():
    # row = departaments.tabeladepartamentos.currentRow()
    # numero = departaments.tabeladepartamentos.item(row, 0).text()
    # nome = departaments.tabeladepartamentos.item(row, 1).text()
    # gerente = departaments.tabeladepartamentos.item(row, 2).text()
    
    # departaments.funcionarios_numero.setPlaceholderText(numero)
    # departaments.funcionarios_nome.setPlaceholderText(nome)
    # departaments.funcionarios_gerente.setPlaceholderText(gerente)

    departaments.close()
    departaments.show()

def chamar_tela_projectsview():
    # row = projects.tabelafuncionarios.currentRow()
    # codigo = projects.tabelafuncionarios.item(row, 0).text()
    # nome = projects.tabelafuncionarios.item(row, 1).text()
    # local = projects.tabelafuncionarios.item(row, 2).text()
    
    # projects.projetos_codigo.setPlaceholderText(codigo)
    # projects.projetos_nome.setPlaceholderText(nome)
    # projects.projetos_local.setPlaceholderText(local)

    projects.close()
    projects.show()

app = QtWidgets.QApplication([])

#CRIAR TELAS
home = uic.loadUi("screens/HomeView.ui")
general = uic.loadUi("screens/GeneralView.ui")
employees = uic.loadUi("screens/EmployeesView.ui")
departaments = uic.loadUi("screens/DepartamentsView.ui")
projects = uic.loadUi("screens/ProjectsView.ui")

#BOTOES CHAMAR TELA
home.entrar.clicked.connect(chamar_tela_generalview)
general.parafuncionarios.clicked.connect(chamar_tela_employeesview)
general.paradepartamentos.clicked.connect(chamar_tela_departamentsview)
general.paraprojetos.clicked.connect(chamar_tela_projectsview)

#BOTOES LOGOUT
general.sair.clicked.connect(logout1)
employees.sair.clicked.connect(logout2)
departaments.sair.clicked.connect(logout3)
projects.sair.clicked.connect(logout4)

home.show()
app.exec()