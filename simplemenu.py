#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        actConfigs = {
                    'options': {
                            'icon': 'preferences.png',
                            'label': '&Preferences',
                            'shortcut': 'Ctrl+P',
                            'hint': 'Configure the application',
                            'action': None
                        },

                    'exit': {
                            'icon': 'exit.png',
                            'label': '&Exit',
                            'shortcut': 'Ctrl+Q',
                            'hint': 'Exit application',
                            'action': qApp.quit
                        }
                }

        actObjects = []

        for actConfig in actConfigs:
            actObject = QAction(QIcon(actConfigs[actConfig]['icon']), actConfigs[actConfig]['label'], self)
            actObject.setShortcut(actConfigs[actConfig]['shortcut'])
            actObject.setStatusTip(actConfigs[actConfig]['hint'])
            if actConfigs[actConfig]['action'] is not None:
                actObject.triggered.connect(actConfigs[actConfig]['action'])
            else:
                pass

            actObjects.append(actObject)


        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        for actObject in actObjects:
            fileMenu.addAction(actObject)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
