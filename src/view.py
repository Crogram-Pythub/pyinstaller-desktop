# -*- coding: utf-8 -*-

import os.path
from os import system
from threading import Thread
from tkinter import (Button, Checkbutton, Entry, IntVar, Label, LabelFrame,
                     StringVar, filedialog)

# from PyInstaller.__main__ import run as pirun

from utils import set_window_center


class View(object):

    def __init__(self, master=None):
        self.root = master
        self.status_build = False
        self.init_view()

    def init_view(self):
        '''基本框架'''
        self.frm_main = LabelFrame(self.root, borderwidth=0)
        self.frm_main.pack(side='left', fill='y')

        self.frm_advance = LabelFrame(self.root, text='高级选项')
        # self.frm_advance.pack(expand='yes', side='right', fill='both', padx=15, pady=10)
        # self.frm_2 = LabelFrame(self.frm_advance, text='高级配置', width=300)
        # self.frm_2.pack(expand='yes', side='top', fill='both', padx=15, pady=10)

        self.frm_project = LabelFrame(self.frm_main, text='项目信息')
        self.frm_config = LabelFrame(self.frm_main, text='配置信息')
        self.frm_operate = LabelFrame(self.frm_main, text='操作')
        self.frm_status = LabelFrame(self.frm_main, text='状态')

        self.frm_project.pack(expand='yes',
                              side='top',
                              fill='both',
                              padx=15,
                              pady=10)
        self.frm_config.pack(fill='x', padx=15, pady=10)
        self.frm_operate.pack(fill='x', padx=15, pady=10)
        self.frm_status.pack(side='bottom', fill='x', padx=15, pady=10)

        self.init_project()
        self.init_config()
        self.init_operate()
        self.init_status()

    def init_project(self):
        '''项目配置'''
        labels = ['入口文件:', '工作目录:', '目标路径:', '图标路径:']

        self.entry_value_list = list()
        for index, label_text in enumerate(labels):
            temp_strvar = StringVar()
            temp_label = Label(self.frm_project, text=label_text)
            temp_entry = Entry(self.frm_project,
                               textvariable=temp_strvar,
                               width=50)
            self.entry_value_list.append(temp_strvar)
            temp_label.grid(row=index % 4,
                            column=0,
                            padx=5,
                            pady=5,
                            sticky='w')
            temp_entry.grid(row=index % 4,
                            column=1,
                            padx=5,
                            pady=5,
                            sticky='we')

        self.btn_main_path = Button(self.frm_project,
                                    text='选择文件',
                                    command=self.fn_select_main)
        self.btn_work_path = Button(self.frm_project,
                                    text='选择路径',
                                    command=self.fn_work_path)
        self.btn_dist_path = Button(self.frm_project,
                                    text='选择路径',
                                    command=self.fn_dist_path)
        self.btn_ico_path = Button(self.frm_project,
                                   text='选择图标',
                                   command=self.fn_icon_path)
        self.btn_main_path.grid(row=0, column=2, padx=5, pady=5, sticky='we')
        self.btn_work_path.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.btn_dist_path.grid(row=2, column=2, padx=5, pady=5, sticky='e')
        self.btn_ico_path.grid(row=3, column=2, padx=5, pady=5, sticky='e')

    def init_config(self):
        '''配置选项'''
        # 定义变量，并初始化
        self.cfg_onefile = IntVar(value=1)
        self.cfg_onedir = IntVar(value=0)
        self.cfg_noconsole = IntVar(value=1)
        self.cfg_clean = IntVar(value=1)
        self.cfg_upx = IntVar(value=1)  # UPX 默认开启
        self.cfg_rename = IntVar()
        self.cfg_exe_name = StringVar()
        # 自定义配置文件
        self.cfg_specfile = StringVar(value='build.spec')
        # 子配置框架
        self.frm_config_base = LabelFrame(self.frm_config,
                                          text='基本',
                                          borderwidth=0)
        self.frm_config_base.pack(fill='x', padx=10, pady=5, ipady=5)
        self.frm_config_exe = LabelFrame(self.frm_config,
                                         text='生成执行文件类型',
                                         borderwidth=0)
        self.frm_config_exe.pack(fill='x', padx=10, pady=5, ipady=5)
        self.frm_config_other = LabelFrame(self.frm_config,
                                           text='其它',
                                           borderwidth=0)
        self.frm_config_other.pack(fill='x', padx=10, pady=5, ipady=5)
        self.frm_config_spec = LabelFrame(self.frm_config,
                                          text='配置文件',
                                          borderwidth=0)
        self.frm_config_spec.pack(fill='x', padx=10, pady=5, ipady=5)

        # 定义按钮
        self.btn_noconsole = Checkbutton(self.frm_config_base,
                                         text='关闭控制台',
                                         variable=self.cfg_noconsole)
        self.btn_clean = Checkbutton(self.frm_config_base,
                                     text='构建前清理',
                                     variable=self.cfg_clean)
        self.btn_upx = Checkbutton(self.frm_config_base,
                                   text='UPX压缩',
                                   variable=self.cfg_upx)
        self.btn_isonefile = Checkbutton(self.frm_config_exe,
                                         text='独立执行文件',
                                         variable=self.cfg_onefile)
        self.btn_isonedir = Checkbutton(self.frm_config_exe,
                                        text='文件夹包含',
                                        variable=self.cfg_onedir)
        self.btn_rename = Checkbutton(self.frm_config_other,
                                      text='修改执行文件名',
                                      variable=self.cfg_rename)
        self.entry_rename = Entry(self.frm_config_other,
                                  textvariable=self.cfg_exe_name)

        # self.btn_rename = Checkbutton(self.frm_config_spec, text='生成配置文件', variable=self.cfg_specfile)
        self.entry_specfile = Entry(self.frm_config_spec,
                                    textvariable=self.cfg_specfile)

        # 放置按钮
        self.btn_isonefile.pack(side='left', fill='x')
        self.btn_isonedir.pack(side='left', fill='x')
        self.btn_noconsole.pack(side='left', fill='x')
        self.btn_clean.pack(side='left', fill='x')
        self.btn_upx.pack(side='left', fill='x')
        self.btn_rename.pack(side='left', fill='x')
        self.entry_rename.pack(fill='x')
        self.entry_specfile.pack(fill='x')

        # 变量自动切换操作
        self.cfg_onefile.trace('w', self.cfg_onefile_trace)
        self.cfg_onedir.trace('w', self.cfg_onedir_trace)

    def cfg_onefile_trace(self, *args):
        '''cfg_onefile 与 cfg_onedir 可以同时不选，但不能同时选中，选中独立执行文件时不能选中文件夹包'''
        if self.cfg_onefile.get() == 1:
            self.cfg_onedir.set(0)

    def cfg_onedir_trace(self, *args):
        '''cfg_onefile 与 cfg_onedir 可以同时不选，但不能同时选中，选中文件夹包含时不能选中独立执行文件'''
        if self.cfg_onedir.get() == 1:
            self.cfg_onefile.set(0)

    def init_operate(self):
        '''操作命令'''
        # 定义按钮
        self.btn_build = Button(self.frm_operate,
                                text='构建生成',
                                command=self.fn_build)
        self.btn_clear = Button(self.frm_operate,
                                text='清理',
                                command=self.fn_clear)
        self.btn_reset = Button(self.frm_operate,
                                text='重置',
                                command=self.fn_reset)
        self.btn_advance = Button(self.frm_operate,
                                  text='高级选项',
                                  command=self.fn_toggle_advance)

        # 放置按钮
        self.btn_build.pack(fill='x', side='left')
        self.btn_clear.pack(fill='x', side='left')
        self.btn_reset.pack(fill='x', side='left')
        self.btn_advance.pack(fill='x', side='right')

    def init_status(self):
        '''状态栏'''
        self.label_status = Label(self.frm_status, text='待命')
        self.label_status.grid(row=1, column=0, padx=5, pady=5, sticky='we')

    def fn_build(self):
        '''生成可执行文件'''
        if len(self.entry_value_list[0].get()) == 0:
            self.label_status['text'] = '请选择源文件'
            return
        if not self.status_build:
            thread_build = Thread(target=self.fn_thread)
            thread_build.setDaemon(True)
            thread_build.start()
        else:
            self.label_status['text'] = '正在打包，请稍后再操作！'

    def fn_thread(self):
        '''线程执行生成动作'''
        self.status_build = True
        self.label_status['text'] = '正在打包，请稍等。。。'
        try:
            cmd = self.fn_build_cmd()
            print(cmd)
            # pirun(cmd)
            system(' '.join(cmd))
            # call(split(' '.join(cmd)), shell=True)
            self.status_build = False
            self.label_status['text'] = '打包成功！'
        except Exception as e:
            self.label_status['text'] = str(e)
            self.status_build = False

    def fn_clear(self):
        '''清理生成文件'''
        pass

    def fn_reset(self):
        '''重置表单内容'''
        for i in range(4):
            self.entry_value_list[i].set('')

        self.cfg_onefile.set(1)
        self.cfg_noconsole.set(1)
        self.cfg_clean.set(1)
        self.cfg_upx.set(1)
        self.cfg_rename.set(0)
        self.cfg_exe_name.set('')

    def fn_toggle_advance(self):
        '''切换高级选项界面'''
        if self.frm_advance.winfo_ismapped():
            set_window_center(self.root, width=(self.root.winfo_width() - 400))
            self.frm_advance.pack_forget()
        else:
            set_window_center(self.root, width=(self.root.winfo_width() + 400))
            self.frm_advance.pack(expand='yes',
                                  side='right',
                                  fill='both',
                                  padx=15,
                                  pady=10)

    def fn_select_main(self):
        '''选择源文件'''
        types = (('py files', '*.py'), ('pyc files', '*.pyc'),
                 ('spec files', '*.spec'), ('All files', '*.*'))
        path = filedialog.askopenfilename(filetypes=types)
        if not path:
            return
        _path = os.path.dirname(path)
        # 主文件
        self.entry_value_list[0].set(path)
        # 工作目录
        self.entry_value_list[1].set(os.path.join(_path, 'build/'))
        # dist目录
        self.entry_value_list[2].set(os.path.join(_path, 'dist/'))

    def fn_work_path(self):
        '''选择工作目录'''
        path = filedialog.askdirectory()
        if not path:
            return
        self.entry_value_list[1].set(path)

    def fn_dist_path(self):
        '''选择生成文件目录'''
        path = filedialog.askdirectory()
        if not path:
            return
        self.entry_value_list[2].set(path)

    def fn_icon_path(self):
        '''选择图标文件'''
        types = (('ico files', '*.ico'), ('icns files', '*.icns'),
                 ('All files', '*.*'))
        path = filedialog.askopenfilename(filetypes=types)
        if not path:
            return
        self.entry_value_list[3].set(path)

    def fn_build_cmd(self, cli=True):
        '''组装命令'''

        cmds = []
        if cli is True:
            # 使用系统命令行
            cmds.append('pyinstaller')
        if len(self.entry_value_list[0].get()) > 0:
            cmds.append(self.entry_value_list[0].get())
        else:
            return cmds
        cmds.append('--windowed')
        cmds.append('-y')
        cmds.append('--noconfirm')
        # cmds.append('--filenames=build.spec')
        # cmds.append('/usr/local/bin/pyinstaller')

        if self.cfg_onefile.get() == 1:
            cmds.append('--onefile')
        elif self.cfg_onedir.get() == 1:
            cmds.append('--onedir')

        if self.cfg_clean.get() == 1:
            cmds.append('--clean')
            cmds.append('--noconfirm')

        if self.cfg_upx.get() == 0:
            cmds.append('--noupx')

        if self.cfg_noconsole.get() == 1:
            cmds.append('--noconsole')

        if len(self.entry_value_list[1].get()) > 0:
            cmds.append('--workpath=' + self.entry_value_list[1].get())

        if len(self.entry_value_list[2].get()) > 0:
            cmds.append('--distpath=' + self.entry_value_list[2].get())

        if len(self.entry_value_list[3].get()) > 0:
            cmds.append('--icon=' + self.entry_value_list[3].get())

        if self.cfg_rename.get() == 1:
            if len(self.cfg_exe_name.get()) > 0:
                cmds.append('--name=' + self.cfg_exe_name.get())

        # print(' '.join(cmds))
        return cmds


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    View(root)
    root.mainloop()
