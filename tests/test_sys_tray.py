import pystray, subprocess
from PIL import Image
import _thread

p = None


def on_quit_clicked(icon):
    if p is None:
        print("进程运行结束")
        icon.stop()
        return 0
    p.terminate()


def spawn_process():
    global p
    p = subprocess.Popen("cmd", shell=True)
    _thread.start_new_thread(wait_exit, tuple())


def wait_exit():
    p.communicate()
    print("进程运行结束")
    icon.stop()
    __import__("sys").exit()


# 创建图标对象
try:
    image = Image.open("ICO.ico")
except FileNotFoundError:
    image = Image.open("tests\\ICO.ico")
menu = (pystray.MenuItem(text="退出", action=on_quit_clicked),)
icon = pystray.Icon("name", image, "托盘名称", menu)

# 显示图标
spawn_process()
icon.run()
