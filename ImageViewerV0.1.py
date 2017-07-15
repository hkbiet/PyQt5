#!/usr/bin/env python


#############################################################################
##
## Please Provide a link to this repo if copying
## author -- Hemant Kumar.
## 
## All rights reserved.
#############################################################################



import os
import sys
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class Central_Widget(QWidget):
	def __init__(self):
		super().__init__()
		#Main function for this class
		self.init_ui()
		#Getting a list of files in an all images directory
		self.filelist = os.listdir()
		self.i=-1
		


	def init_ui(self):
		#Adding Butttons for navigation
		self.previous = QPushButton('Previous image')
		self.next = QPushButton('Next image')
		
		#Adding layout for buttons
		self.h_box = QHBoxLayout()
		self.h_box.addWidget(self.previous)
		self.h_box.addWidget(self.next)
		
		#Adding this layout for adding Horizontal layout containing horizontally arranged buttons
		self.v_box = QVBoxLayout()
		self.v_box.addLayout(self.h_box)

		self.l = QLabel('                  Click Next or Previous Button to view images in this directory')
		filelist=os.listdir()
		length = len(filelist)
		#filename=filelist[29]
		initial=0
		#self.l.setPixmap(QPixmap(filename))
		self.next.clicked.connect(self.next_click)
		self.previous.clicked.connect(self.previous_click)


		self.v_box.addWidget(self.l)
		self.setLayout(self.v_box)
		self.show()

	def next_click(self):
		'''Code for Next button event '''
		self.i+=1
		#print(self.i)
		self.l.setPixmap(QPixmap(self.filelist[self.i]))

	def previous_click(self):
		''' Code for Previous button event'''
		self.i-=1
		print(self.i)
		self.l.setPixmap(QPixmap(self.filelist[self.i]))




class Main_Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.CW_Object = Central_Widget()
		self.setCentralWidget(self.CW_Object)
		self.init_ui()


	def init_ui(self):
		
		self.statusBar()	



		self.setWindowTitle('Image Viewer')
		self.show()


if __name__=='__main__':
	app = QApplication(sys.argv)
	win = Main_Window()
	sys.exit(app.exec_())
