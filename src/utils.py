# _*_ coding:utf-8 _*_
# utils functions


def set_window_center(window, width=None, height=None, minsize=True, resize=False):
    """设置窗口宽高及居中"""
    # 获取窗口宽高
    if width == None or height == None:
        # 宽高为 None 时取窗口自身大小
        window.update_idletasks() # 更新
        window.withdraw() # 隐藏重绘
        # window.update() # 获取窗口宽高之前需要先刷新窗口
    if width is None:
        width = window.winfo_width()
    if height is None:
        height = window.winfo_height()

    # 获取屏幕宽高
    w_s = window.winfo_screenwidth()
    h_s = window.winfo_screenheight()

    # 计算 x, y 位置
    x_co = (w_s - width) / 2
    y_co = (h_s - height) / 2

    # 设置窗口宽高和居中定位
    window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
    window.deiconify() # 显示
    # 是否设置窗口最小尺寸
    if minsize:
        window.minsize(width, height)
    # 是否可调整大小
    if resize:
        window.resizable(True, True)
    else:
        window.resizable(False, False)


def get_screen_size(window):
    """获取屏幕 宽、高"""
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    """获取窗口 宽、高"""
    window.update()
    return window.winfo_width(), window.winfo_height()


def treeview_sort_column(tv, col, reverse):
    """Treeview、列名、排列方式"""
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    # print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        # print(k)
    tv.heading(col, command=lambda: treeview_sort_column(
        tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
