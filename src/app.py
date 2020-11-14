# -*- coding: utf-8 -*-

from os import system
from threading import Thread
from tkinter import Tk
# from shlex import split
# from subprocess import call

from utils import set_window_center
from view import View
# import PyInstaller
# import PyInstaller.__main__

class App(View):
    def __init__(self, master=None):
        super(App, self).__init__()

    def fn_build(self):
        '''生成可执行文件'''
        if not self.status_build:
            thread_build = Thread(target=self.fn_thread)
            thread_build.setDaemon(True)
            thread_build.start()
        else:
            self.label_status['text'] = '正在打包，请稍后再操作！'

    def fn_thread(self):
        '''线程执行生成动作'''
        if len(self.entry_value_list[0].get()) == 0:
            self.label_status['text'] = '请选择源文件'
            return
        self.status_build = True
        cmd = self.fn_build_cmd()
        print(cmd)
        self.label_status['text'] = '正在打包，请稍等。。。'
        try:
            # PyInstaller.__main__.run(cmd)
            system(' '.join(cmd))
            # call(split(' '.join(cmd)), shell=True)
            self.status_build = False
            self.label_status['text'] = '打包成功！'
        except Exception as e:
            self.label_status['text'] = str(e)
            self.status_build = False

if __name__ == '__main__':
    root = Tk()
    root.title('GUI应用生成器')
    App(root)
    set_window_center(root)
    root.mainloop()
