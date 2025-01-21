batch_data = """
echo msgbox "test" > sb.vbs
sb.vbs
del sb.vbs
"""
import os.path
import sys

if not hasattr(sys, "_MEIPASS"):
    print("该程序需要在pyinstaller中运行")
    exit.__call__()
# print(os.path.join(sys._MEIPASS, "tmp.bat"), sys._MEIPASS)
if os.path.exists(os.path.join(sys._MEIPASS, "tmp.bat")):
    os.remove(os.path.join(sys._MEIPASS, "tmp.bat"))
with open(os.path.join(sys._MEIPASS, "tmp.bat"), "w+") as f:
    f.write(batch_data)
f.close()
os.system('"' + os.path.join(sys._MEIPASS, "tmp.bat") + '"')
os.remove('"' + os.path.join(sys._MEIPASS, "tmp.bat") + '"')
