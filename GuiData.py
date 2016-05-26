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

class GuiData(QtGui.QWidget):
    def __init__(self, parent = None):
        
        super(GuiData, self).__init__(parent)
        
        self.PolygonList = []
        self.PreTime = 0
    
        self.LPyList = []
        self.RPyList = []
        self.LTextList = []
        self.RTextList = []
        self.LeftX = 0
        self.LeftY = 500
        self.RightX = 500
        self.RightY = 500
        
        self.DeltaY = 100.0

        pass
    @QtCore.pyqtSlot(int)
    def AddDFlow(self, BufSz):
        self.AddFlow(0, BufSz)
        pass
    @QtCore.pyqtSlot(int)
    def AddAFlow(self, BufSz):
        self.AddFlow(1, BufSz)
        pass
    def getPolyNum(self):
        return len(self.PolygonList)
    def getPolyList(self, i):
        return self.PolygonList[i]
    def getLPyNum(self):
        return len(self.LPyList)
    def getLPyList(self, i):
        return self.LPyList[i]
    def getRPyNum(self):
        return len(self.RPyList)
    def getRPyList(self, i):
        return self.RPyList[i]
    def setPolyList(self, Poly, i):
        self.PolygonList[i] = Poly
        pass
    def setPreTime(self, pretime):
        self.PreTime = pretime
        pass
    def setDeltaY(self, dy):
        self.DeltaY = dy
        pass
    def setWnd(self, lx, ly, rx, ry):
        self.LeftX = lx
        self.LeftY = ly
        self.RightX = rx
        self.RightY = ry
        pass
    def Translate(self, dx, dy):
        for i in range(1, len(self.PolygonList) + 1):
            self.PolygonList[i - 1].translate(dx, dy)
        for i in range(1, len(self.LPyList) + 1):
            self.LPyList[i - 1].setY(self.LPyList[i - 1].y() - 1)
        for i in range(1, len(self.RPyList) + 1):
            self.RPyList[i - 1].setY(self.RPyList[i - 1].y() - 1)
    def AddFlow(self, attri, size):
        if attri == 0:
            p1 = QtCore.QPoint(self.LeftX, self.LeftY)
            p2 = QtCore.QPoint(self.RightX, self.RightY + self.DeltaY)
            p3 = QtCore.QPoint(self.RightX, self.RightY + self.DeltaY + size / 16.0)
            p4 = QtCore.QPoint(self.LeftX, self.LeftY + size / 16.0)
            self.AddPolygon(p1, p2, p3, p4)
            self.LPyList.append(p1)
            self.LTextList.append('sender puts %d bytes to buffer'%size)
            pass
        elif attri == 1:
            p1 = QtCore.QPoint(self.RightX, self.RightY)
            p2 = QtCore.QPoint(self.LeftX, self.LeftY + self.DeltaY)
            p3 = QtCore.QPoint(self.LeftX, self.LeftY + self.DeltaY)
            p4 = QtCore.QPoint(self.RightX, self.RightY)
            self.AddPolygon(p1, p2, p3, p4)
            self.RPyList.append(p1)
#            self.RTextList.append('sender puts %d bytes to buffer'%size)
            pass
    def AddPolygon(self, p1, p2, p3, p4):
        tmpList = []
        tmpList.append(p1)
        tmpList.append(p2)
        tmpList.append(p3)
        tmpList.append(p4)
        self.PolygonList.append(QtGui.QPolygon(tmpList))
        pass
    def ClearPolygon(self):
        self.PolygonList = []
        self.LPyList = []
        self.RPyList = []