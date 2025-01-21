# run.py

from subprocess import *
import threading
import time

p = Popen(
    "inside_py\\python -m PyInstaller -F temps\\sb.py",
    shell=True,
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE,
)


def run():
    global p
    while True:
        line = p.stdout.readline()
        if not line:  # 空则跳出
            line = p.stderr.readline()
        if not line:
            break
        print(">>>>>>", line.decode("GBK"))
        p.stdout.flush()
        p.stderr.flush()

    print("look up!!! EXIT ===")  # 跳出


w = threading.Thread(target=run)
w.start()
