#No Tochka_S_Zapyatoy's
import subprocess
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QComboBox, QLineEdit, QPushButton, QCheckBox, QWidget
from PyQt6.QtCore import QSize
import wget
import os


def backup(password):
    wget.download("https://telegram.org/dl/desktop/win64_portable", "tportable.zip")
    os.mkdir("telegram")
    subprocess.run(["powershell", "-Command", "Expand-Archive -LiteralPath tportable.zip -DestinationPath telegram"])
    subprocess.run(["powershell", "-Command", "telegram/Telegram.exe"])


app = QApplication([])
window = QMainWindow()
window.setWindowTitle("WinToLin")
window.setFixedSize(QSize(500, 370))
window.setWindowIcon(QIcon("Images/icon.png"))
startLabel = QLabel("Select distribution that you want to use (if you don't know, select first)", window)
startLabel.setFixedSize(500, 10)
startLabel.move(30, 40)
dropdownDistribution = QComboBox(window)
dropdownDistribution.addItem(QIcon("Images/minticon.png"), 'Linux Mint')
dropdownDistribution.addItem(QIcon("Images/archicon.png"), 'Arch Linux')
dropdownDistribution.addItem(QIcon("Images/debianicon.png"), 'Linux Debian')
dropdownDistribution.addItem(QIcon("Images/fedoraicon.png"), 'Fedora Linux')
dropdownDistribution.addItem(QIcon("Images/manjaroicon.png"), 'Manjaro Linux')
dropdownDistribution.addItem(QIcon("Images/opensuseicon.png"), 'OpenSUSE Linux')
dropdownDistribution.move(170, 60)
dropdownDistribution.setFixedSize(150, 50)
cloudLabel = QLabel("Enter password for your .zip archive", window)
cloudLabel.move(150, 100)
cloudLabel.setFixedSize(250, 50)
inputPassword = QLineEdit(window)
inputPassword.move(50, 150)
inputPassword.setFixedSize(400, 50)
checkbox = QCheckBox("I understand the risk \nto lost my files and I \nwant to reinstall the system", window)
checkbox.move(160, 200)
checkbox.setFixedSize(200, 100)
start = QPushButton("Start", window)
settings = QPushButton("Settings", window)
settingsWindow = QWidget()
settingsWindow.setWindowTitle("WinToLin Settings")
settingsWindow.setFixedSize(QSize(300, 100))
languageLabel = QLabel("Select language", settingsWindow)
languageLabel.move(100, 0)
dropdownLanguage = QComboBox(settingsWindow)
dropdownLanguage.addItem(QIcon("Images/minticon.png"), 'English')
dropdownLanguage.addItem(QIcon("Images/minticon.png"), 'Русский')
dropdownLanguage.move(100, 20)
start.move(200, 300)
settings.move(0, 0)
start.setCheckable(True)
checkbox.setCheckable(True)


def ShowSettings():
    settingsWindow.show()


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
        backup(inputPassword)


start.clicked.connect(Start)
settings.clicked.connect(ShowSettings)
window.show()
app.exec()
