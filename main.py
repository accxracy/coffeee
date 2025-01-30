import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6 import QtWidgets
from UI.ui_form import Ui_Form
from UI.ui_main import Ui_MainWindow


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
        with sqlite3.connect('data/coffee.sqlite') as db:
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
