#No Tochka_S_Zapyatoy's
import subprocess
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QComboBox, QLineEdit, QPushButton, QCheckBox, QWidget, QFileDialog, QListView, QAbstractItemView
from PyQt6.QtCore import QSize
import wget
import os
import datetime
import sys


def backup(password):
    wget.download("https://telegram.org/dl/desktop/win64_portable", "tportable.zip")
    os.mkdir("telegram")
    subprocess.run(["powershell", "-Command", "Expand-Archive -LiteralPath tportable.zip -DestinationPath telegram"])
    subprocess.run(["powershell", "-Command", "telegram/Telegram.exe"])


app = QApplication([])
window = QMainWindow()
window.setWindowTitle("WinToLin")
window.setFixedSize(QSize(500, 370))
window.setWindowIcon(QIcon("Images/icon.jpg"))
startLabel = QLabel("Select distribution that you want to use (if you don't know, select first)", window)
startLabel.setFixedSize(500, 15)
startLabel.move(30, 40)
dropdownDistribution = QComboBox(window)
dropdownDistribution.addItem(QIcon("Images/minticon.png"), 'Linux Mint')
dropdownDistribution.addItem(QIcon("Images/archicon.png"), 'Arch Linux')
dropdownDistribution.addItem(QIcon("Images/debianicon.png"), 'Linux Debian')
dropdownDistribution.addItem(QIcon("Images/fedoraicon.png"), 'Fedora Linux')
dropdownDistribution.addItem(QIcon("Images/manjaroicon.png"), 'Manjaro Linux')
dropdownDistribution.addItem(QIcon("Images/opensuseicon.png"), 'OpenSUSE Linux')
dropdownDistribution.addItem(QIcon("Images/kaliicon.png"), 'Kali Linux')
dropdownDistribution.addItem(QIcon("Images/windows.png"), 'Linux Wubuntu')
dropdownDistribution.move(170, 65)
dropdownDistribution.setFixedSize(150, 42)
cloudLabel = QLabel("Enter password for your .zip archive", window)
cloudLabel.move(150, 145)
cloudLabel.setFixedSize(250, 50)
inputPassword = QLineEdit(window)
inputPassword.move(50, 190)
inputPassword.setFixedSize(400, 35)
selectLabel = QLabel("Select files for backup", window)
selectLabel.move(70, 110)
selectLabel.setFixedSize(250, 50)
checkbox = QCheckBox("I understand the risk \nto lost my files and I \nwant to reinstall the system", window)
checkbox.move(160, 210)
checkbox.setFixedSize(200, 100)
slowDevice = QCheckBox("Slow device", window)
slowDevice.move(350, 37)
slowDevice.setFixedSize(200, 100)
start = QPushButton("Start", window)
settings = QPushButton(QIcon("Images/settingsicon.jpg"),"Settings", window)
info = QPushButton("About", window)
selectFiles = QPushButton("Select files", window)
start.move(200, 300)
settings.move(0, 0)
info.move(400, 0)
selectFiles.move(320, 120)
selectFiles.setFixedSize(110, 30)
start.setCheckable(True)
checkbox.setCheckable(True)


settingsWindow = QWidget()
settingsWindow.setWindowTitle("WinToLin Settings")
settingsWindow.setFixedSize(QSize(300, 100))
languageLabel = QLabel("Select language", settingsWindow)
languageLabel.move(100, 0)
dropdownLanguage = QComboBox(settingsWindow)
dropdownLanguage.addItem(QIcon("Images/americanflag.png"), 'English')
dropdownLanguage.addItem(QIcon("Images/russianflag.jpg"), 'Русский')
dropdownLanguage.move(100, 20)
ok = QPushButton("OK", settingsWindow)
ok.move(100, 50)


infoWindow = QWidget()
infoWindow.setWindowTitle("About WinToLin")
infoWindow.setFixedSize(QSize(500, 370))
infoLabel = QLabel("WinToLin is an application for simply switch Windows to Linux. \nInstuctions: \n1.Select Linux distribution that you want to install \n2.Select files that you want to backup \n3.Create password for .zip archive with your files \n4.Press Start \n42.Wait 7.5 millions of years ;-) \n5.Follow to instructions of application \n\nMade by RubyLeoCompany", infoWindow)


fileSelecter = QFileDialog()
fileSelecter.setWindowTitle("Select files for backup with WinToLin")
fileSelecter.setMinimumSize(500, 370)
fileview = fileSelecter.findChild(QListView, 'listView')
if fileview:
    fileview.setSelectionMode(QAbstractItemView.MultiSelection)


def Translate():
    if dropdownLanguage.currentIndex() == 0:
        languageLabel.setText("Select language")
        startLabel.setText("Select distribution that you want to use (if you don't know, select first)")
        cloudLabel.setText("Enter password for your .zip archive")
        checkbox.setText("I understand the risk \nto lost my files and I \nwant to reinstall the system")
        slowDevice.setText("Slow device")
        start.setText("Start")
        settings.setText("Settings")
        info.setText("About")
        settingsWindow.setWindowTitle("WinToLin Settings")
        infoWindow.setWindowTitle("About WinToLin")
        infoLabel.setText("WinToLin is an application for simply switch Windows to Linux. \nInstuctions: \n1.Select Linux distribution that you want to install \n2.Select files that you want to backup \n3.Create password for .zip archive with your files \n4.Press Start \n42.Wait 7.5 millions of years ;-) \n5.Follow to instructions of application \n\nMade by RubyLeoCompany")
        selectFiles.setText("Select files")
        selectLabel.setText("Select files for backup")
        fileSelecter.setWindowTitle("Select files for backup with WinToLin")
    elif dropdownLanguage.currentIndex() == 1:
        languageLabel.setText("Выберите язык")
        startLabel.setText("Выберите желаемый дистрибутив Linux (если вы не знаете, выберите первый)")
        cloudLabel.setText("Задайте пароль .zip архиву \nс вашими данными")
        checkbox.setText("Я осознаю риск \nпотери моих файлов \nи хочу переустановить \nсистему")
        slowDevice.setText("Слабое устройство")
        start.setText("Старт")
        settings.setText("Настройки")
        info.setText("О программе")
        settingsWindow.setWindowTitle("Настройки WinToLin")
        infoWindow.setWindowTitle("О программе WinToLin")
        infoLabel.setText("WinToLin - программа для простого прехода с Windows на Linux. \nИнструкция: \n1.Выберите дистрибутив Linux, который хотите установить \n2.Выберите файлы, которые вы хотите сохранить \n3.Создайте пароль для .zip-архива с вашими файлами \n4.Нажмите Старт \n42.Подождите 7.5 миллионов лет ;-) \n5.Следуйте появившимся инструкциям \n\nСделано студией RubyLeoCompany")
        selectFiles.setText("Выберите файлы")
        selectLabel.setText("Выберите файлы для сохранения")
        fileSelecter.setWindowTitle("Выберите файлы для сохранения через WinToLin")


def ShowSettings():
    settingsWindow.show()


def ShowInfo():
    infoWindow.show()


def ShowFileSelecter():
    fileSelecter.show()


def Start():
    if checkbox.isChecked():
        if dropdownDistribution.currentIndex() == 0:
            subprocess.run(["powershell", "-File", "mintisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 1:
            subprocess.run(["powershell", "-File", "archisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 2:
            subprocess.run(["powershell", "-File", "debianisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 3:
            subprocess.run(["powershell", "-File", "fedoraisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 4:
            subprocess.run(["powershell", "-File", "manjaroisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 5:
            subprocess.run(["powershell", "-File", "opensuseisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 6:
            subprocess.run(["powershell", "-File", "kaliisodownload.ps1"], capture_output=True, text=True)
        elif dropdownDistribution.currentIndex() == 7:
            subprocess.run(["powershell", "-File", "wubuntuisodownload.ps1"], capture_output=True, text=True)
        backup(inputPassword)
    

#def FilesToZip():
    


#print(datetime.today().year+range(1, 100, 1))
start.clicked.connect(Start)
settings.clicked.connect(ShowSettings)
ok.clicked.connect(Translate)
info.clicked.connect(ShowInfo)
selectFiles.clicked.connect(ShowFileSelecter)
window.show()
app.exec()
