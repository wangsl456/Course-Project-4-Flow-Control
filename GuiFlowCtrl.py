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
from FlowData import *
from Flow import *

class GuiFlowCtrl(QtGui.QWidget):
    def __init__(self, parent = None):
        
        super(GuiFlowCtrl, self).__init__(parent)
        
        self.FlowData = FlowData(self)
        
        self.PreTime = 0
        self.start = False
        self.pasue = False
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.TimerAction)
        
        self.IdxCnt = 0
        
        self.White = QtGui.QColor(255, 255, 255)
        self.Blue = QtGui.QColor(0, 0, 100)
        self.Green = QtGui.QColor(0, 255, 0)
        self.Yellow = QtGui.QColor(150, 150, 0)
        self.Violet = QtGui.QColor(0 , 0, 200)
        self.Gray = QtGui.QColor(135, 135, 135)
        self.Black = QtGui.QColor(0, 0, 0)
        self.Pink = QtGui.QColor( 200, 0, 50)
        self.ColorDict = {0 : self.White, 1 : self.Blue, 2 : self.Green, 3 : self.Yellow, 4 : self.Violet, 5 : self.Pink}
#        self.StartAction()
        pass
    def StartAction(self):
        self.timer.start(20)
        self.FlowData.InitState()
        self.FlowData.GuiData.ClearPolygon()
        self.start = True
        pass
    def StopAction(self):
#        self.timer.stop()
        self.start = False
        pass
    def ReAction(self):
        self.start = True
        self.timer.start(20)
    def TimerAction(self):
        if self.start:
            self.PreTime += 20
            self.FlowData.RandAction()
            if self.FlowData.ProcData():
                self.FlowData.SendBufSz = 0
                self.timer.stop()
            self.FlowData.GuiData.Translate(0, -1)
            pass
        else:
            self.PreTime += 20
            self.FlowData.ProcData()
            self.FlowData.GuiData.Translate(0, -1)
            pass
            self.timer.stop()
            pass
    def setWnd(self, lx, ly, rx, ry):
        self.FlowData.GuiData.setWnd(lx, ly, rx, ry)
        pass
    def draw(self, qp, posx, posy, size):
        
        x = posx
        y = posy
        sz = size
        
        qp.setPen(self.Black)
        for i in range(1, self.FlowData.GuiData.getLPyNum() + 1):
            tmpPoint = QtCore.QPoint(x + 5, self.FlowData.GuiData.getLPyList(i - 1).y())
            qp.drawLine(tmpPoint, self.FlowData.GuiData.getLPyList(i - 1))
            qp.drawText(tmpPoint, self.FlowData.GuiData.LTextList[i - 1])
            pass
        for i in range(1, self.FlowData.GuiData.getRPyNum() + 1):
            tmpPoint = QtCore.QPoint(x + sz.width() - 5, self.FlowData.GuiData.getRPyList(i - 1).y())
            qp.drawLine(tmpPoint, self.FlowData.GuiData.getRPyList(i - 1))
        qp.setPen(self.Blue)
        qp.setBrush(self.Blue)
        for i in range(1, self.FlowData.GuiData.getPolyNum() + 1):
            tmpPolyList = self.FlowData.GuiData.getPolyList(i - 1)
            qp.drawPolygon(tmpPolyList, self.FlowData.GuiData.getPolyNum())
            qp.drawLine(tmpPolyList[0], tmpPolyList[-1])
            pass
        qp.setPen(self.Green)
        qp.setBrush(self.Green)
        qp.drawRect(x + 10, y + 5 + sz.height() * 7.0 / 8.0 +sz.height() / 100.0, self.FlowData.SendBufSz * 1.0 / self.FlowData.SendMaxBufSz * (sz.width() / 5.0 - 20), sz.height() / 30.0)
        qp.drawRect(x + 10 + sz.width() * 4.0 / 5.0, y + 5 + sz.height() * 7.0 / 8.0 +sz.height() / 100.0, self.FlowData.RecvBufSz * 1.0 / self.FlowData.RecvMaxBufSz * (sz.width() / 5.0 - 20), sz.height() / 30.0)
        qp.drawRect(x + 10, y + 5 + sz.height() * 37.0 / 40.0 +sz.height() / 100.0, self.FlowData.SendAppSz * 1.0 / self.FlowData.SendMaxAppSz * (sz.width() / 5.0 - 20), sz.height() / 30.0)
        qp.drawRect(x + 10 + sz.width() * 4.0 / 5.0, y + 5 + sz.height() * 37.0 / 40.0 +sz.height() / 100.0, self.FlowData.RecvAppSz * 1.0 / self.FlowData.RecvMaxAppSz * (sz.width() / 5.0 - 20), sz.height() / 30.0)
        pass