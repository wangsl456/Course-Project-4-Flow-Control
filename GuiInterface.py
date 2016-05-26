#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Course Project 4
GUI_FlowControl

author: Junyong Wang

last edited: May 2016
"""
import sys, random
from PyQt4 import QtGui, QtCore
from GuiFlowCtrl import *

class GuiInterface(QtGui.QWidget):
    def __init__(self, parent = None):
        super(GuiInterface, self).__init__(parent)
        
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.TimerAction)
        self.timer.start(20)
        
        self.DisplayWidget = GuiFlowCtrl(parent)
        
        self.White = QtGui.QColor(255, 255, 255)
        self.Blue = QtGui.QColor(0, 0, 100)
        self.Green = QtGui.QColor(0, 255, 0)
        self.Yellow = QtGui.QColor(150, 150, 0)
        self.Violet = QtGui.QColor(0 , 0, 200)
        self.Gray = QtGui.QColor(135, 135, 135)
        self.Black = QtGui.QColor(0, 0, 0)
        self.Pink = QtGui.QColor( 200, 0, 50)
        self.ColorDict = {0 : self.White, 1 : self.Blue, 2 : self.Green, 3 : self.Yellow, 4 : self.Violet, 5 : self.Pink}
        
        pass
    def draw(self, qp):
        
        x = self.x()
        y = self.y()
        sz = self.size()
        self.DisplayWidget.setWnd(self.x() + self.size().width() / 5.0, self.y() + self.size().height(), self.x() + self.size().width() * 4.0 / 5.0, self.y() + self.size().height())
        qp.setPen(self.Black)
        qp.drawRect(x, y, sz.width(), sz.height())
        qp.drawLine(x + sz.width() / 5.0, y, x + sz.width() / 5.0, y + sz.height())
        qp.drawLine(x + sz.width() * 4.0 / 5.0, y, x + sz.width() * 4.0 / 5.0, y + sz.height())
        qp.drawRect(x + 5, y + 5 + sz.height() * 7.0 / 8.0, sz.width() / 5.0 - 10, sz.height() / 10.0)
        qp.drawLine(x + 5, y + 5 + sz.height() * 37.0 / 40.0, x - 5 + sz.width() / 5.0, y + 5 + sz.height() * 37.0 / 40.0)
        qp.drawRect(x + 5 + sz.width() * 4.0 / 5.0, y + 5 + sz.height() * 7.0 / 8.0, sz.width() / 5.0 - 10, sz.height() / 10.0)
        qp.drawLine(x + 5 + sz.width() * 4.0 / 5.0, y + 5 + sz.height() * 37.0 / 40.0, x - 5 + sz.width(), y + 5 + sz.height() * 37.0 / 40.0)
        self.DisplayWidget.draw(qp, x, y, sz)
        pass
    def StartAction(self):
        self.DisplayWidget.StartAction()
        pass
    def StopAction(self):
        self.DisplayWidget.StopAction()
        pass
    def ReAction(self):
        self.DisplayWidget.ReAction()
    def TimerAction(self):
        self.update()
        pass
    def setFileSz(self, fsz):
        self.DisplayWidget.FlowData.setFileSz(fsz)
        pass
    def setBufSz(self, bsz):
        self.DisplayWidget.FlowData.setBufSz(bsz)
        pass
    def setPropaTime(self, pt):
        self.DisplayWidget.FlowData.setPropagationTime(pt * 1000)
        self.DisplayWidget.FlowData.GuiData.setDeltaY(pt * 50)
        pass