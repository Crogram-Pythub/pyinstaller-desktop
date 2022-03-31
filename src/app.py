# -*- coding: utf-8 -*-

from tkinter import Tk

from utils import set_window_center
from view import View

class App(Tk):
    '''
    App

    应用程序主窗体，所有窗口、组件的根级窗口
    '''

    def __init__(self):
        Tk.__init__(self)
        self.title('PyInstaller Desktop')
        View(self)
        set_window_center(self)
        self.mainloop()


if __name__ == '__main__':
    App()
