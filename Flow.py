#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Course Project 4
Flow Control

author: Junyong Wang

last edited: May 2016
"""
import sys, random

class Flow():
    def __init__(self, attri, sz, idx):
        self.Index = idx
        self.Attribute = attri
        self.Size = sz
        pass
    def SetAttribute(self, attri):
        self.Attribute = attri
        pass
    def GetAttribute(self):
        return self.Attribute
        pass
    def SetSize(self, sz):
        self.Size = sz
        pass
    def GetSize(self):
        return self.Size
    def GetIndex(self):
        return self.Index