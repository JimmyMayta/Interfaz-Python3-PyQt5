import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Inicio(object):
    def __init__(self):
        self.Font = QtGui.QFont()
        self.Font.setFamily("Lato")

    def IniPrincipal(self, MaiWin, App):
        MaiWin.setObjectName("MaiWin")

        Screen = App.desktop().screenGeometry()
        ScreenWidth, ScreenHeight = Screen.width(), Screen.height()

        Width, Height = 390, 290

        MaiWin.setWindowTitle("Login")
        MaiWin.move(((ScreenWidth / 2) - (Width / 2)), ((ScreenHeight / 2) - (Height / 2) - 100))
        MaiWin.resize(Width, Height)

        MaiWin.setMinimumSize(QtCore.QSize(Width, Height))
        MaiWin.setMaximumSize(QtCore.QSize(Width, Height))

        self.IniWid = QtWidgets.QWidget(MaiWin)
        self.IniWid.setObjectName("IniWid")

        self.Font.setPointSize(19)
        self.Font.setBold(True)

        self.Titulo = QtWidgets.QLabel(self.IniWid)
        self.Titulo.setObjectName("Titulo")
        self.Titulo.setText("Login")
        self.Titulo.setGeometry(QtCore.QRect(10, 13, 370, 60))
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setFont(self.Font)

        self.Font.setPointSize(12)
        self.Font.setBold(False)

        self.UsuLinEdi = QtWidgets.QLineEdit(self.IniWid)
        self.UsuLinEdi.setObjectName("UsuLinEdi")
        self.UsuLinEdi.setPlaceholderText('Usuario')
        self.UsuLinEdi.setGeometry(QtCore.QRect(45, 90, 300, 33))
        self.UsuLinEdi.setFont(self.Font)
        self.UsuLinEdi.setAlignment(QtCore.Qt.AlignCenter)
        self.UsuLinEdi.setFrame(False)

        self.ConLinEdi = QtWidgets.QLineEdit(self.IniWid)
        self.ConLinEdi.setObjectName("ConLinEdi")
        self.ConLinEdi.setPlaceholderText('Contraseña')
        self.ConLinEdi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConLinEdi.setGeometry(QtCore.QRect(45, 139, 300, 33))
        self.ConLinEdi.setFont(self.Font)
        self.ConLinEdi.setAlignment(QtCore.Qt.AlignCenter)
        self.ConLinEdi.setFrame(False)

        self.Font.setBold(True)

        self.InicioPusBut = QtWidgets.QPushButton(self.IniWid)
        self.InicioPusBut.setText("Inicio")
        self.InicioPusBut.setGeometry(QtCore.QRect(120, 210, 160, 30))
        self.InicioPusBut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.InicioPusBut.setFont(self.Font)

        MaiWin.setCentralWidget(self.IniWid)
        QtCore.QMetaObject.connectSlotsByName(MaiWin)


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    Ini = Inicio()
    Ini.IniPrincipal(Main, App)
    Main.show()
    sys.exit(App.exec_())