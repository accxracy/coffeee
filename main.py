import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1303, 594)
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
        self.search.setGeometry(QtCore.QRect(130, 110, 93, 28))
        self.search.setObjectName("search")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(131, 2, 361, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.any_type = QtWidgets.QRadioButton(parent=self.widget)
        self.any_type.setText("")
        self.any_type.setObjectName("any_type")
        self.gridLayout.addWidget(self.any_type, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.molotiy = QtWidgets.QRadioButton(parent=self.widget)
        self.molotiy.setText("")
        self.molotiy.setObjectName("molotiy")
        self.gridLayout.addWidget(self.molotiy, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.zerna = QtWidgets.QRadioButton(parent=self.widget)
        self.zerna.setText("")
        self.zerna.setObjectName("zerna")
        self.gridLayout.addWidget(self.zerna, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.price_limit = QtWidgets.QLineEdit(parent=self.widget)
        self.price_limit.setObjectName("price_limit")
        self.gridLayout.addWidget(self.price_limit, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 26))
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


class Coffe_Viewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Список Кофе')
        self.tableWidget.setFixedSize(1220, 320)
        self.setFixedSize(1303, 594)
        self.search.clicked.connect(self.search_with_params)

        self.show_info(self.get_info())

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
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Сорт', 'Мтепень обжарки', 'Молотый / в Зёрнах', 'Описание вкуса', 'Цена(руб.)', 'Объем упаковки'])

        for row_idx, row in enumerate(rows):
            for col_idx, item in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(item)))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(171)

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