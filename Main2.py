#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Course Project 4
Flow Control

author: Junyong Wang

last edited: May 2016
"""

import sys, random
from PyQt4 import QtGui, QtCore
from GuiInterface import *
class Widget(QtGui.QWidget):
    
    def __init__(self):
        
        super(Widget, self).__init__()
        self.initUI()
        pass
        
    def initUI(self):
        self.isStart = False
        self.isPause = False
        self.gui = GuiInterface(self)
        #Push Button Init
        
        self.btn = QtGui.QPushButton("Start")
        self.btn_ = QtGui.QPushButton("Pause")
        #LCD Init
        self.lcd_filesz = QtGui.QLCDNumber(5, self)
        self.lcd_bufsz = QtGui.QLCDNumber(4, self)
        self.lcd_propatime = QtGui.QLCDNumber(2, self)
        self.lcd_filesz.display(4096)
        self.lcd_bufsz.display(2048)
        self.lcd_propatime.display(2)
        #Label Init
        self.label_filesz = QtGui.QLabel('file size')
        self.label_bufsz = QtGui.QLabel('buffer size')
        self.label_propatime = QtGui.QLabel('propagation time')
        self.label_pause = QtGui.QLabel('pause')
        self.label_start = QtGui.QLabel('start')
        
        #Slider Init
        self.sld_filesz = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sld_bufsz = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sld_propatime = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        
        #grid Init
        grid = QtGui.QGridLayout()
        
        grid.setSpacing(10)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 1)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(3, 1)
        grid.addWidget(self.label_filesz, 0, 0)
        grid.addWidget(self.label_bufsz, 0, 1)
        grid.addWidget(self.label_propatime, 0, 2)
        grid.addWidget(self.label_pause, 0, 3)
        grid.addWidget(self.sld_filesz, 1, 0)
        grid.addWidget(self.sld_bufsz, 1, 1)
        grid.addWidget(self.sld_propatime, 1,2)
        grid.addWidget(self.lcd_filesz, 2, 0)
        grid.addWidget(self.lcd_bufsz, 2, 1)
        grid.addWidget(self.lcd_propatime, 2,2)
        grid.addWidget(self.label_start, 2, 3)
        grid.addWidget(self.btn_, 1, 4)
        grid.addWidget(self.btn, 2, 4)
        QtCore.QObject.connect(self.btn, QtCore.SIGNAL("clicked()"), self.Start)
        QtCore.QObject.connect(self.btn_, QtCore.SIGNAL("clicked()"), self.Pause)
        
        grid.addWidget(self.gui, 3, 0, 1, 8)
        
        self.sld_propatime.setRange(2, 5)
        self.sld_propatime.setValue(2)
        self.sld_propatime.setPageStep(0.5)
        
        self.sld_filesz.setRange(4096, 10240)
        self.sld_filesz.setValue(4096)
        self.sld_filesz.setSingleStep(512)
        self.sld_filesz.setPageStep(512)
        
        self.sld_bufsz.setRange(2048, 8192)
        self.sld_bufsz.setValue(2048)
        self.sld_bufsz.setSingleStep(512)
        self.sld_bufsz.setPageStep(512)
        
        self.setLayout(grid)
        
        self.sld_propatime.valueChanged.connect(self.lcd_propatime.display)
        self.sld_filesz.valueChanged.connect(self.lcd_filesz.display)
        self.sld_bufsz.valueChanged.connect(self.lcd_bufsz.display)
        
        self.sld_propatime.valueChanged.connect(self.gui.setPropaTime)
        self.sld_filesz.valueChanged.connect(self.gui.setFileSz)
        self.sld_bufsz.valueChanged.connect(self.gui.setBufSz)
        
        self.showMaximized()
        self.setWindowTitle('Flow Control')
        self.show()
        
        pass
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.gui.draw(qp)
        qp.end()
        pass
    def Start(self):
        if self.isStart == False:
            self.gui.StartAction()
            self.isStart = True
            self.btn.setText('stop')
            pass
        elif self.isStart == True:
            self.gui.StopAction()
            self.isStart = False
            self.btn.setText('restart')
            pass
        pass
    def Pause(self):
        if self.isPause == False:
            self.gui.StopAction()
            self.isPause = True
        elif self.isPause == True:
            self.gui.ReAction()
            self.isPause = False
        pass
def main():
    
    #Init Class Var
    
    app = QtGui.QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    main()