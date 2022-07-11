import modules.appui as appui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from typing import *


class HomePage():
    def __init__(self, MainWindow: QMainWindow, ui: appui.Ui_MainWindow) -> None:
        self._APP_VERSION = 'v0.4.2'
        self._MainWindow = MainWindow
        self._ui = ui
