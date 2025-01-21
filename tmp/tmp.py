

executing_thing='''
@echo off
set my_files='''+__import__("os").path.join(__import__("sys")._MEIPASS,"my_files")+'''
@echo on
echo test
 
'''
import os,sys
TEMPDIR=sys._MEIPASS
with open(os.path.join(TEMPDIR,'tmp.bat'),'w+',encoding='ansi')as f:
    f.write(executing_thing)
os.system('"'+os.path.join(TEMPDIR,'tmp.bat')+'"')

