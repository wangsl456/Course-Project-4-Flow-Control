#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Course Project 4
Flow Control Data

author: Junyong Wang

last edited: May 2016
"""
import sys, random
from Flow import *
from GuiData import *
from PyQt4 import QtGui, QtCore

class FlowData(QtGui.QWidget):
    AddDataFlow = QtCore.pyqtSignal(int)
    AddACKFlow = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        super(FlowData, self).__init__(parent)
        self.GuiData = GuiData()
        
        self.FileSz = 4096
        self.BufSz = 2048
        self.PropagationTime = 2000
        self.SendRate = 0.8
        self.RemainFileSz = 0
        self.SendMaxBufSz = 2048
        self.RecvMaxBufSz = 2048
        self.SendBufSz = 0
        self.RecvBufSz = 0
        
        self.SendBufRate = 1024
        self.RecvBufRate = 1024
        self.SendAppRate = 1024
        self.RecvAppRate = 1024
        
        self.SendAppSz = 0
        self.RecvAppSz = 0
        self.SendMaxAppSz = 4096
        self.RecvMaxAppSz = 4096
        self.CosumeSz = 2048
        
        self.LastRecv = False
        
        self.FlowList = []
        
        self.IdxCnt = 0
        
        self.SenderAction = 'Wait'
        self.SenderTimer = QtCore.QTimer()
        QtCore.QObject.connect(self.SenderTimer, QtCore.SIGNAL("timeout()"), self.RecvDataAction)
        self.RecverAction = 'Wait'
        self.RecverTimer = QtCore.QTimer()
        QtCore.QObject.connect(self.RecverTimer, QtCore.SIGNAL("timeout()"), self.RecvACKAction)
        self.InitState()
        self.ConnectSigSlot()
        
        self.Threshold = 1000
        self.Value = 0
        pass
    
    def ConnectSigSlot(self):
        self.AddDataFlow.connect(self.GuiData.AddDFlow)
        self.AddACKFlow.connect(self.GuiData.AddAFlow)
        pass
    def InitState(self):
        self.SenderAction = 'SendFlow'
        self.RecverAction = 'WaitFlow'
        self.SendState = 'Hold'
        self.RecvState = 'Hold'
        self.Value = 0
        self.SendBufSz = 0
        self.RecvBufSz = 0
        self.RemainFileSz = self.FileSz
        self.SendMaxAppSz = self.FileSz
        self.RecvMaxAppSz = self.FileSz
        self.SendMaxBufSz = self.BufSz
        self.RecvMaxBufSz = self.BufSz
        pass
    def AddFlow(self, attri, sz):
        f = Flow(attri, sz, self.IdxCnt)
        self.FlowList.append(f)
        self.IdxCnt += 1
        pass
    def GetFlow(self):
        return self.FlowList
    def RandAction(self):
        self.Value += random.randint(0, 10)
        if self.Value >= self.Threshold:
            self.Value = 0
            if self.RecvBufSz != 0:
                self.RecvAppSz +=self.RecvBufSz
                self.RecvBufSz =0
    def ProcData(self):
        if self.SenderAction == 'SendFlow':
            if self.RemainFileSz == 0:
                return 1
            self.SenderAction = 'WaitACK'
            self.SendBufSz = min(self.RemainFileSz, self.BufSz)
            self.AddFlow(0, self.SendBufSz)
            self.AddDataFlow.emit(self.SendBufSz)
            self.SenderTimer.start(self.PropagationTime + self.SendBufSz / self.SendRate)
            self.RemainFileSz -= self.SendBufSz
            pass
        if self.SenderAction == 'SendACK':
            if self.RemainFileSz == 0:
                return 1
            self.SenderAction = 'WaitACK'
            self.AddFlow(0, 0)
            self.AddDataFlow.emit(0)
            self.SenderTimer.start(self.PropagationTime)
            pass
        if self.RecverAction == 'SendACK0':
            self.RecverAction = 'WaitACK'
            self.AddFlow(1, 0)
            self.AddACKFlow.emit(0)
            self.RecverTimer.start(self.PropagationTime)
            pass
        if self.RecverAction == 'SendACK1':
            self.RecverAction = 'WaitFlow'
            self.AddFlow(1, 0)
            self.AddACKFlow.emit(0)
            self.RecverTimer.start(self.PropagationTime)
            pass
        return 0
        pass
    def RecvDataAction(self):
        self.SenderTimer.stop()
        if self.RecvBufSz == 0:
            if self.RecverAction == 'WaitFlow':
                self.RecvBufSz += self.SendBufSz
            pass
        if self.RecvBufSz == 0:
            self.RecverAction = 'SendACK1'
        else:
            self.RecverAction = 'SendACK0'
            self.RecverTimer.start(self.PropagationTime)
            pass
        pass
    
    def RecvACKAction(self):
        self.RecverTimer.stop()
        if self.RecverAction == 'WaitACK':
            self.SenderAction = 'SendACK'
            pass
        elif self.RecverAction =='WaitFlow':
            self.SenderAction = 'SendFlow'
        self.SenderTimer.stop()
        pass
    def setFileSz(self, fsz):
        self.FileSz = fsz
        pass
    def setBufSz(self, bsz):
        self.BufSz = bsz
        pass
    def setPropagationTime(self, pt):
        self.PropagationTime = pt
        pass