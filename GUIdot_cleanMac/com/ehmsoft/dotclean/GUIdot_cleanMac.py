# -*- coding: utf-8 -*-
'''
Created on 08/07/2012

@author: elfotografo007
'''
#GUIdot_cleanMac.py
#Aplicacion para solucionar el problema de los archivos ._ en Mac
__version__ = '0.1'

import os
import sys
import shutil
import copy
from PySide.QtCore import *
from PySide.QtGui import *
import resources

class GUIdot_cleanMac(QDialog):
    def __init__(self, parent = None):
        super(GUIdot_cleanMac, self).__init__(parent)
        siguiente_btn = QPushButton('Siguiente')
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Seleccione memoria:'))
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(siguiente_btn)
        self.lista = QListWidget()
        self.lista.addItems(self.getNodos())
        layout.addWidget(self.lista)
        layout.addLayout(hlayout)
        layout.addWidget(QLabel('Hecho por: www.ehmsoft.com'))
        self.setLayout(layout)
        self.connect(siguiente_btn, SIGNAL('clicked()'), self.siguienteClicked)
        self.setWindowTitle('Dot Clean')

    def getNodos(self): #Lista todos los volumenes y quita el Disco Duro del sistema
        path = '/Volumes'
        folders = os.listdir(path)
        try:
            folders.remove('Macintosh HD')
        except ValueError:
            carpetas = copy.copy(folders)
            for folder in carpetas:
                if os.path.isdir(os.path.join('/Volumes', folder)):
                    if os.path.exists(os.path.join('/Volumes', folder, 'Applications')):
                        folders.remove(folder)
        finally:
            return folders
        
    def dot_clean(self, path):
        return os.system('dot_clean %s' % path)
    
    def siguienteClicked(self):
        selected = self.lista.currentItem().text()
        path = os.path.join('/Volumes', selected)
        if self.dot_clean(path) == 0:
            title = 'Proceso exitoso'
            msg = u'Se limpió la memoria con éxito'
        else:
            title = 'Proceso fallido'
            msg = u'Ocurrió un error inesperado. Verifique que la memoria esté montada.'
        QMessageBox.information(self, title, msg)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName("ehmSoftware")
    app.setOrganizationDomain("ehmsoft.com")
    app.setApplicationName("Dot Clean")
    app.setWindowIcon(QIcon(":/images/icono.png"))
    ventana = GUIdot_cleanMac()
    ventana.show()
    ventana.raise_()
    sys.exit(app.exec_())


