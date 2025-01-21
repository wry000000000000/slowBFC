batch_data='''
echo msgbox "test" > sb.vbs
sb.vbs
del sb.vbs
'''
import os.path

if os.path.exists(".\\tmp.bat"):
    os.remove(".\\tmp.bat")
with open(".\\tmp.bat","w+")as f:
    f.write(batch_data)
f.close()
os.system(".\\tmp")
os.remove(".\\tmp.bat")