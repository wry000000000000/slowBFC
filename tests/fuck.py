import ctypes

ctypes.windll.shell32.ShellExecuteW(
    None,
    "runas",
    "cmd",
    r"/c del E:\Projects\slowBFC\tmp\my_files && pause",
    None,
    1,
)
