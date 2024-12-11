import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 735)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.desc_coffee = QtWidgets.QLineEdit(parent=Form)
        self.desc_coffee.setGeometry(QtCore.QRect(220, 250, 351, 151))
        self.desc_coffee.setObjectName("desc_coffee")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 657, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 420, 571, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.price_coffee = QtWidgets.QLineEdit(parent=self.widget)
        self.price_coffee.setObjectName("price_coffee")
        self.gridLayout.addWidget(self.price_coffee, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.volume_coffee = QtWidgets.QLineEdit(parent=self.widget)
        self.volume_coffee.setObjectName("volume_coffee")
        self.gridLayout.addWidget(self.volume_coffee, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(parent=Form)
        self.widget1.setGeometry(QtCore.QRect(10, 50, 571, 191))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.coffee_sort = QtWidgets.QLineEdit(parent=self.widget1)
        self.coffee_sort.setObjectName("coffee_sort")
        self.gridLayout_2.addWidget(self.coffee_sort, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.roast_coffee = QtWidgets.QComboBox(parent=self.widget1)
        self.roast_coffee.setObjectName("roast_coffee")
        self.roast_coffee.addItem("")
        self.roast_coffee.addItem("")
        self.roast_coffee.addItem("")
        self.gridLayout_2.addWidget(self.roast_coffee, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 2)
        self.type_coffee = QtWidgets.QComboBox(parent=self.widget1)
        self.type_coffee.setObjectName("type_coffee")
        self.type_coffee.addItem("")
        self.type_coffee.addItem("")
        self.gridLayout_2.addWidget(self.type_coffee, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.pushButton.setText(_translate("Form", "Ок"))
        self.label_5.setText(_translate("Form", "Цена(руб.)"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
        self.label.setText(_translate("Form", "Сорт"))
        self.label_2.setText(_translate("Form", "Степень ображки"))
        self.roast_coffee.setItemText(0, _translate("Form", "Средняя"))
        self.roast_coffee.setItemText(1, _translate("Form", "Тёмная"))
        self.roast_coffee.setItemText(2, _translate("Form", "Светлая"))
        self.label_3.setText(_translate("Form", "Молотый/в зёрнах"))
        self.type_coffee.setItemText(0, _translate("Form", "Молотый"))
        self.type_coffee.setItemText(1, _translate("Form", "В зёрнах"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1333, 597)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 1281, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search.setGeometry(QtCore.QRect(130, 130, 93, 28))
        self.search.setObjectName("search")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(131, 2, 361, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.any_type = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.any_type.setText("")
        self.any_type.setObjectName("any_type")
        self.gridLayout.addWidget(self.any_type, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.molotiy = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.molotiy.setText("")
        self.molotiy.setObjectName("molotiy")
        self.gridLayout.addWidget(self.molotiy, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.zerna = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.zerna.setText("")
        self.zerna.setObjectName("zerna")
        self.gridLayout.addWidget(self.zerna, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.price_limit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.price_limit.setObjectName("price_limit")
        self.gridLayout.addWidget(self.price_limit, 3, 1, 1, 2)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1100, 140, 191, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QPushButton(parent=self.widget)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(parent=self.widget)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1333, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "кофе)"))
        self.search.setText(_translate("MainWindow", "поиск!"))
        self.label_5.setText(_translate("MainWindow", "Любой тип"))
        self.label_2.setText(_translate("MainWindow", "Молотый"))
        self.label_3.setText(_translate("MainWindow", "В зернах"))
        self.label_4.setText(_translate("MainWindow", "Цена(до):"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.edit_button.setText(_translate("MainWindow", "Изменить"))


class NewWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Coffe_Viewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Список Кофе')
        self.setFixedSize(1300, 594)
        self.search.clicked.connect(self.search_with_params)
        self.add_button.clicked.connect(self.open_window_add)
        self.edit_button.clicked.connect(self.open_window_edit)
        self.show_info(self.get_info())

    def edit_coffe_from_db(self, ID, sort, roast, type, desc, price, volume):
        query = """UPDATE coffee SET sort = ?, roasting = ?, type = ?, desc = ?, price = ?, volume = ? WHERE ID = ?"""
        values = (sort, roast, type, desc, price, volume, ID)
        self.execute_with_params(query, values)
        self.show_info(self.get_info())

    def add_coffe_to_db(self, sort, roast, type, desc, price, volume):
        query = """INSERT INTO coffee (sort, roasting, type, desc, price, volume) VALUES (?, ?, ?, ?, ?, ?)"""
        values = (sort, roast, type, desc, price, volume)
        self.execute_with_params(query, values)
        self.show_info(self.get_info())

    def edit_coffe(self):
        current_row = self.tableWidget.currentRow()
        if current_row != -1:
            id_coffee = int(self.tableWidget.item(current_row, 0).text())
            s = self.newwind.coffee_sort.text()
            r = self.newwind.roast_coffee.currentText()
            t = self.newwind.type_coffee.currentText()
            d = self.newwind.desc_coffee.text()
            p = self.newwind.price_coffee.text()
            v = self.newwind.volume_coffee.text()
            self.edit_coffe_from_db(id_coffee, s, r, t, d, p, v)
            self.newwind.close()

    def add_coffee(self):
        s = self.newwind.coffee_sort.text()
        r = self.newwind.roast_coffee.currentText()
        t = self.newwind.type_coffee.currentText()
        d = self.newwind.desc_coffee.text()
        p = self.newwind.price_coffee.text()
        v = self.newwind.volume_coffee.text()
        self.add_coffe_to_db(s, r, t, d, p, v)
        self.newwind.close()

    def open_window_add(self):
        self.newwind = NewWindow()
        self.newwind.show()
        self.newwind.setWindowTitle('Кофе!(новая запись)')
        self.newwind.pushButton.clicked.connect(self.add_coffee)

    def open_window_edit(self):
        self.newwind = NewWindow()
        self.newwind.show()
        self.newwind.setWindowTitle('Кофе!(изменить запись)')
        self.newwind.pushButton.clicked.connect(self.edit_coffe)

    def execute_with_params(self, query, values=None):
        with sqlite3.connect('coffee.sqlite') as db:
            cur = db.cursor()
            if values:
                cur.execute(query, values)

            else:
                cur.execute(query)
        return cur.fetchall()

    def get_info(self):
        return self.execute_with_params("SELECT * FROM coffee")

    def show_info(self, param):
        rows = param

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]) if rows else 0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Сорт', 'Cтепень обжарки', 'Молотый / в Зёрнах', 'Описание вкуса', 'Цена(руб.)', 'Объем упаковки'])

        for row_idx, row in enumerate(rows):
            for col_idx, item in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(162)
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(4, 400)

    def search_with_params(self):
        molot = self.molotiy.isChecked()
        zern = self.zerna.isChecked()
        price = self.price_limit.text()
        if molot:
            if price:
                query = "SELECT * FROM coffee WHERE type = 'Молотый' AND price < ?"
                values = (price,)
                self.show_info(self.execute_with_params(query, values))

            else:
                query = "SELECT * FROM coffee WHERE type = 'Молотый'"
                self.show_info(self.execute_with_params(query))
        elif zern:
            if price:
                query = "SELECT * FROM coffee WHERE type = 'В зернах' AND price < ?"
                values = (price,)
                self.show_info(self.execute_with_params(query, values))

            else:
                query = "SELECT * FROM coffee WHERE type = 'В зернах'"
                self.show_info(self.execute_with_params(query))
        else:
            if price:
                query = "SELECT * FROM coffee WHERE price < ?"
                values = (price,)
                self.show_info(self.execute_with_params(query, values))
            else:
                self.show_info(self.get_info())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffe_Viewer()
    ex.show()
    sys.exit(app.exec())
