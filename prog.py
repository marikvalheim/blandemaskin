# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:21:45 2018

@author: Win10User


C:\python>pyuic5 -x firstgui.ui -o firstgui.py


C:\WinPython-64bit-3.6.3.0Qt5\scripts>pyuic5 -x c:\git\Python\QTDesigner\firstgui.ui -o c:\git\Python\QTDesigner\firstgui.py

C:\WinPython-64bit-3.6.3.0Qt5>python c:\git\Python\QTDesigner\prog.py

"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from firstgui import Ui_myfirstgui

#import socket
#UDP_IP = "192.168.1.123"
#UDP_PORT = 6789
#MESSAGE = ""

#print("UDP target IP:", UDP_IP)
#print("UDP target port:", UDP_PORT )
#print("message:", MESSAGE)



class MyFirstGuiProgram(Ui_myfirstgui):
    def __init__(self, dialog):
        Ui_myfirstgui.__init__(self)
        self.setupUi(dialog)
        
        # Connect "dial" dialog with a custom function (onDialValueChanged)
        
        self.pushButton_1.clicked.connect(self.MIX)
        self.Vatn.valueChanged.connect(self.onVatnValueChanged)
        self.Saft.valueChanged.connect(self.onSaftValueChanged)
        self.Vodka.valueChanged.connect(self.onVodkaValueChanged)
        
    def onSaftValueChanged(self, value):
        print("Saft %d" % value)
        self.Number_Saft.setSegmentStyle(2) # Flat segment
        palette = self.Number_Saft.palette()
        self.Number_Saft.setProperty("value", value)                
        
    def onVatnValueChanged(self, value):
        print("Vatn %d" % value)
        self.Number_Vatn.setSegmentStyle(2) # Flat segment
        palette = self.Number_Vatn.palette()
        self.Number_Vatn.setProperty("value", value)

        
    def onVodkaValueChanged(self, value):
        print("Vodka %d" % value)
        self.Number_Vodka.setSegmentStyle(2) # Flat segment
        palette = self.Number_Vodka.palette()
        self.Number_Vodka.setProperty("value", value)
        

      
    def MIX(self,value):
        print("miksar")
        a = self.Saft.value()
        print("Saft %d" % a)
        QtCore.QTimer.singleShot(a*100,self.stopPumpA)  
        
        b = self.Vodka.value()
        print("Vodka %d" % b)
        QtCore.QTimer.singleShot(b*100,self.stopPumpB)  
        
        c = self.Vatn.value()
        print("Vatn %d" % c)
        QtCore.QTimer.singleShot(c*100,self.stopPumpC)  
        
        
    def stopPumpA(self):
        print("Saft stop")
        
    def stopPumpB(self):
        print("Vodka stop")
        
    def stopPumpC(self):
        print("Vatn stop")
        

                

        
        
        #sock = socket.socket(socket.AF_INET, # Internet
        #                     socket.SOCK_DGRAM) # UDP
        
        #MESSAGE = "%d" % value
        #sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
        


        

         
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    
    prog = MyFirstGuiProgram(dialog)
    
    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
