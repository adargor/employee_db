import sys
import sqlite3
from MainWindow import Ui_MainWindow
from EditorWindow import Ui_EditorWindow
from DepWindow import Ui_DepWindow
from AddWindow import Ui_AddWindow
from ErrWindow import Ui_ErrWindow
from SearchWindow import Ui_SearchWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.refresh()
        self.ui.empTable.resizeColumnsToContents()
        #Коннекты кнопок
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.departmentButton.clicked.connect(self.dep)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.editButton.clicked.connect(self.edit)
        self.ui.deleteButton.clicked.connect(self.delete)
        #Контекстное меню для таблицы
        self.ui.empTable.addAction(self.ui.actionEdit)
        self.ui.empTable.addAction(self.ui.actionDelete)
        self.ui.actionDelete.triggered.connect(self.delete)
        self.ui.actionEdit.triggered.connect(self.edit)
        #Коннект двойного щелчка по ряду с вызовом окна редактора
        self.ui.empTable.doubleClicked.connect(self.edit)
    def refresh(self):
        #Создаём список dbData и заполняем его данными всех сотрудников
        dbData = []
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM employee"):
            temp = []
            for entry in row:
                temp.append(entry)
            dbData.append(temp)
        conn.close()

        #Указываем количество рядов, которые отображает виджет таблицы
        self.ui.empTable.setRowCount(len(dbData))
        #Показываем количество сотрудников в статусбаре
        self.statusBar().showMessage('Сотрудников в базе: {}'.format(len(dbData)))
        #Заполняем виджет таблицы данными из листа
        for record in dbData:
            m = dbData.index(record)
            for value in record:
                n = record.index(value)
                newitem = QtWidgets.QTableWidgetItem(str(value))
                self.ui.empTable.setItem(m,n,newitem)
    def add(self):
        addWindow = Add()
        addWindow.exec_()
        addWindow.raise_()
    def delete(self):
        #Проверяем, выбрана ли строка
        if not self.ui.empTable.selectedItems():
            Error.popup_error(self, "Не выбран сотрудник")
        else:
            selectedId = self.ui.empTable.selectedItems()[0].text()
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("DELETE FROM employee WHERE Id = {}".format(int(selectedId)))
            conn.commit()
            conn.close()
            self.refresh()
    def edit(self):
        #Проверяем, выбрана ли строка
        if not self.ui.empTable.selectedItems():
            Error.popup_error(self, "Не выбран сотрудник")
        else:
            id = window.ui.empTable.selectedItems()[0].text()
            name = window.ui.empTable.selectedItems()[1].text()
            age = window.ui.empTable.selectedItems()[2].text()
            job = window.ui.empTable.selectedItems()[3].text()
            department = window.ui.empTable.selectedItems()[4].text()

            editorWindow = Editor(id, name, age, job, department)
            editorWindow.exec_()
            editorWindow.raise_()
    def dep(self):
        depWindow = Departments()
        depWindow.exec_()
        depWindow.raise_()
    def search(self):
        searchWindow = Search()
        searchWindow.exec_()
        searchWindow.raise_()

class Editor(QtWidgets.QDialog):
    def __init__(self, id, name, age, job, department):
        QtWidgets.QWidget.__init__(self)
        self.id = id
        self.name = name
        self.age = age
        self.job = job
        self.department = department

        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)

        #Populating departments list
        self.departments = []
        self.departments_list = []
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        for row in c.execute("SELECT DISTINCT department from departments"):
            self.departments.append(row)
        for item in self.departments:
            self.ui.departmentBox.addItem(item[0])
            for value in item:
                self.departments_list.append(value)

        self.ui.ageLine.setValidator(QIntValidator(1,120))
        self.ui.idLine.setText(self.id)
        self.ui.nameLine.setText(self.name)
        self.ui.ageLine.setText(self.age)
        self.ui.jobLine.setText(self.job)
        self.ui.btnCommit.clicked.connect(self.commit)
        self.ui.departmentBox.setCurrentIndex(self.departments_list.index(self.department))

    def commit(self):
        id = self.ui.idLine.text()
        name = self.ui.nameLine.text()
        age = self.ui.ageLine.text()
        job = self.ui.jobLine.text()
        department = self.ui.departmentBox.currentText()
        if id and name and age and job and department:
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("UPDATE employee SET name='{0}', age={1}, job_title='{4}',department='{3}' WHERE id={2}".format(name,age,id,department,job))
            conn.commit()
            conn.close()
            self.close()
            window.refresh()
        else:
            Error.popup_error(self, "Все поля должны быть заполнены")

class Add(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.name = ""
        self.age = ""
        self.job = ""
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self)
        self.ui.ageLine.setValidator(QIntValidator(1,120))
        self.ui.nameLine.setText(self.name)
        self.ui.ageLine.setText(self.age)
        self.ui.jobLine.setText(self.job)
        self.ui.btnCommit.clicked.connect(self.commit)
        #Populating departments list
        departments = []
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        for row in c.execute("SELECT DISTINCT department from departments"):
            departments.append(row)
        for item in departments:
            self.ui.departmentBox.addItem(item[0])



    def commit(self):
        name = self.ui.nameLine.text()
        age = self.ui.ageLine.text()
        job = self.ui.jobLine.text()
        department = self.ui.departmentBox.currentText()
        if name and age and job and department:
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            #Пишем в БД
            c.execute("INSERT INTO employee VALUES (null,'{0}',{1},'{2}','{3}')".format(name,age,job,department))
            # #Коммитим
            conn.commit()
            # #Закрываем подключение
            conn.close()
            # #Обновляем экран
            window.refresh()
            self.close()
        else:
            Error.popup_error(self, "Все поля должны быть заполнены")

class Departments(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DepWindow()
        self.ui.setupUi(self)
        self.refresh()
        #Button bindings
        self.ui.exitDepButton.clicked.connect(self.close)
        self.ui.addDepButton.clicked.connect(self.add)
        self.ui.delDepButton.clicked.connect(self.delete)
        self.ui.lineEditDep.setText("Введите название отдела")
    def refresh(self):
        dbData = []
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM departments"):
            temp = []
            for entry in row:
                temp.append(entry)
            dbData.append(temp)
        conn.close()

        #Указываем количество рядов, которые отображает виджет таблицы
        self.ui.depTable.setRowCount(len(dbData))
        #Заполняем виджет таблицы данными из листа
        for record in dbData:
            m = dbData.index(record)
            for value in record:
                n = record.index(value)
                newitem = QtWidgets.QTableWidgetItem(str(value))
                self.ui.depTable.setItem(m,n,newitem)
    def add(self):
        if self.ui.lineEditDep.text():
            dep_name = self.ui.lineEditDep.text()
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            #Пишем в БД
            c.execute("INSERT INTO departments VALUES (null,'{}')".format(dep_name))
            # #Коммитим
            conn.commit()
            # #Закрываем подключение
            conn.close()
            # #Обновляем экран
            self.refresh()
    def delete(self):
        #Проверяем, выбрана ли строка
        if not self.ui.depTable.selectedItems():
            Error.popup_error(self, "Не выбран отдел")
        else:
            #Проверяем, есть ли сотрудники в выбранном для удаления отделе
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            dep_to_delete = self.ui.depTable.selectedItems()[1].text()
            check_dep = c.execute("SELECT COUNT(*) FROM employee WHERE department like '{0}'".format(dep_to_delete))
            check_dep = check_dep.fetchall()[0][0]
            if not check_dep:
                selectedId = self.ui.depTable.selectedItems()[0].text()
                conn = sqlite3.connect('employee.db')
                c = conn.cursor()
                c.execute("DELETE FROM departments WHERE Id = {}".format(int(selectedId)))
                conn.commit()
                conn.close()
                self.refresh()
            else:
                Error.popup_error(self, "В выбранном отделе есть сотрудники")

class Error(QtWidgets.QDialog):
    def __init__(self, message):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_ErrWindow()
        self.ui.setupUi(self)
        self.ui.label.setText(message)
        self.ui.errButton.clicked.connect(self.close)

    def popup_error(self, message):
        errWindow = Error(message)
        errWindow.exec_()
        errWindow.raise_()

class Search(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.update_departments()
        #Button bindings
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.searchButton.clicked.connect(self.search)
        #Actions bindings
        self.ui.searchTable.addAction(self.ui.actionEdit)
        self.ui.actionEdit.triggered.connect(self.edit)
        self.ui.searchTable.addAction(self.ui.actionDelete)
        self.ui.actionDelete.triggered.connect(self.delete)
        #Editor window on double click
        self.ui.searchTable.doubleClicked.connect(self.edit)

    def update_departments(self):
        '''Заполняет combobox списком всех отделов'''
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        for row in c.execute('SELECT DISTINCT department from departments'):
            self.ui.departmentBox.addItem(row[0])

    def search(self):
        name = self.ui.nameLine.text()
        job = self.ui.jobLine.text()
        department = self.ui.departmentBox.currentText()

        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        dbData = []
        for row in c.execute("SELECT * FROM employee WHERE name like '%{0}%' "
                             "AND job_title like '%{1}%' "
                             "AND department like '%{2}%'".format(name, job, department)):
            temp = []
            for entry in row:
                temp.append(entry)
            dbData.append(temp)
        conn.close()

        self.ui.searchTable.setRowCount(len(dbData))

        for record in dbData:
            m = dbData.index(record)
            for value in record:
                n = record.index(value)
                newitem = QtWidgets.QTableWidgetItem(str(value))
                self.ui.searchTable.setItem(m,n,newitem)

        self.ui.searchTable.resizeColumnsToContents()

    def edit(self):
        id = self.ui.searchTable.selectedItems()[0].text()
        name = self.ui.searchTable.selectedItems()[1].text()
        age = self.ui.searchTable.selectedItems()[2].text()
        job = self.ui.searchTable.selectedItems()[3].text()
        department = self.ui.searchTable.selectedItems()[4].text()

        editorWindow = Editor(id, name, age, job, department)
        editorWindow.exec_()
        editorWindow.raise_()
        self.search()
        window.refresh()

    def delete(self):
        selectedId = self.ui.searchTable.selectedItems()[0].text()
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("DELETE FROM employee WHERE Id = {}".format(int(selectedId)))
        conn.commit()
        conn.close()
        self.search()
        window.refresh()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())