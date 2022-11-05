import os, shutil, psutil
import platform, socket, uuid, re, keyboard, sys, webbrowser, requests
import version
from datetime import datetime
from tkinter import messagebox
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

def check_update():
    local_version = version.ver
    try:
        response = requests.get('https://raw.githubusercontent.com/Jesewe-Hack/lzq-optimizer/main/version.py').text
    except:
        messagebox.showerror(f"LZQ Optimizer", "Failed to get latest version", icon='info')
        response = None
    if response != None:
        github_version = float(re.split('=', response.strip())[1])
        if github_version > local_version:
            messagebox.showinfo('LZQ Optimizer', f'Found new version: {github_version}', icon='info')
            try:
                webbrowser.open('https://github.com/Jesewe-Hack/lzq-optimizer/releases')
            except:
                messagebox.showinfo("LZQ Optimizer", "No updates found!", icon='info')
        else:
            messagebox.showinfo("LZQ Optimizer", "No updates found!", icon='info')

def exit():
    os.abort()

def temp_cleaner():  
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'
    deleteFileCount = 0
    deleteFolderCount = 0
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print( '%s file deleted' % itemName )
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                print( '%s folder deleted' % itemName )
                deleteFolderCount = deleteFolderCount + 1
        except Exception as e:
            print('Access Denied: %s' % itemName )
    messagebox.showinfo("LZQ Optimizer", "Temp folder cleared successfully!", icon='info')

def dump_cleaner():  
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/CrashDumps'
    deleteFileCount = 0
    deleteFolderCount = 0
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print( '%s file deleted' % itemName )
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                print( '%s folder deleted' % itemName )
                deleteFolderCount = deleteFolderCount + 1

        except Exception as e:
            print('Access Denied: %s' % itemName )
    messagebox.showinfo("LZQ Optimizer", "Dump folder cleared successfully!", icon='info')

if __name__ == '__main__':
    Form, Window = uic.loadUiType("gui.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    form.pushButton.clicked.connect(temp_cleaner)
    form.pushButton_2.clicked.connect(dump_cleaner)
    form.label_4.setText(f'System: {platform.system()}\nVersion: {platform.version()}\n\nIP Address: {socket.gethostbyname(socket.gethostname())}')
    form.pushButton_3.clicked.connect(exit)
    form.pushButton_4.clicked.connect(check_update)
    app.exec()