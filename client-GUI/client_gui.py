#!/usr/local/bin/python3

# imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import sys

#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
#from PyQt5.QtGui import QIcon

class App(QWidget):

	def __init__(self):
		super().__init__()

		self.title = "OSL Exchange Live Watchlist"
		self.left = 600
		self.top = 350
		self.width = 300
		self.height = 200
		self.init_UI()

	def init_UI(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.create_table()

        # Add box layout, add table to box layout and add box layout to widget
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

        # Show widget
		self.show()

	def create_table(self):

		# Create table
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(2)

		self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
		self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
		self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
		self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
		self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
		self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))

		self.tableWidget.move(0,0)

        # table selection change
		#self.tableWidget.doubleClicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):

		print("\n")

		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == "__main__":

	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
