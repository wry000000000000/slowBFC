from __future__ import print_function
import ctypes, sys, os

if len(sys.argv) < 2:
    raise ValueError("此exe需要一个参数：被删除路径。")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # 将要运行的代码加到这里
    print("executed:", f"del {sys.argv[1]}")
    os.remove(sys.argv[1])
else:
    if not hasattr(sys, "_MEIPASS"):
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                f"{__file__} {sys.argv[1]}",
                None,
                1,
            )
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                unicode(sys.executable),
                unicode(f"{__file__} {sys.argv[1]}"),
                None,
                1,
            )
    else:
        print("getting admin...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", f"{sys.executable}", f"{sys.argv[1]}", None, 1
        )
