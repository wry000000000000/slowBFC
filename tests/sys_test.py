import sys

try:
    print(
        sys._MEIPASS,
    )
except:
    pass
try:
    print(sys.executable, __file__)
except:
    pass
