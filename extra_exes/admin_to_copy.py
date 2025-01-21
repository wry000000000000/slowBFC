from __future__ import print_function
import ctypes, sys, os

if len(sys.argv) < 3:
    raise ValueError("此exe需要两个参数：被复制路径、复制路径。")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # 将要运行的代码加到这里
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
    print("executed:", f"copy {sys.argv[1]} {sys.argv[2]}")
    os.system(f"copy {sys.argv[1]} {sys.argv[2]}")
else:
    if not hasattr(sys, "_MEIPASS"):
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                f"{__file__} {sys.argv[1]} {sys.argv[2]}",
                None,
                1,
            )
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                unicode(sys.executable),
                unicode(f"{__file__} {sys.argv[1]} {sys.argv[2]}"),
                None,
                1,
            )
    else:
        print("getting admin...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", f"{sys.executable}", f"{sys.argv[1]} {sys.argv[2]}", None, 1
        )
