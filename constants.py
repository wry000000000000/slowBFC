import sys, os


class Flag(object):
    def __init__(self, num: int, name: str):
        self.num, self.name = [num, name]

    def __int__(self) -> int:
        return self.num

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return repr(self.num) + "." + repr(self)


ADMIN_FLAG = Flag(0, "use_admin")
TASK_BAR_CLOSE_FLAG = Flag(1, "use_taskbar_to_close")
END_TO_PAUSE_FLAG = Flag(2, "pause_when_ended")
SAME_NAME_FLAG = Flag(3, "use_same_name_with_bat_file")

DEBUG = False

TEMP = sys._MEIPASS if hasattr(sys, "_MEIPASS") else ".\\tmp"
PKL_LOCATION = "." if DEBUG else os.path.expanduser("~\\.slowBFC")

EDITOR_KEYWORDS = [
    "echo",
    "start",
    "if",
    "not",
    "for",
    "del",
    "copy",
    "cls",
    "goto",
    "cd",
    "set",
    "pause",
]

MIT_LICENSE_TEXT = """Copyright ( C ) Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files ( the "Software" ) , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
B_WEBSITE = "https://space.bilibili.com/3493122243824372?spm_id_from=333.1007.0.0"
G_WEBSITE = "https://github.com/wry000000000000/slowBFC"
THE_VERSION_TEXT = """# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers={filevers},
    prodvers={provers},
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x0,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '040904E4',
        [StringStruct('CompanyName', '{company_name}'),
        StringStruct('FileDescription', '{fd}'),
        StringStruct('FileVersion', '{plain_fv}'),
        StringStruct('InternalName', '{plain_in}'),
        StringStruct('LegalCopyright', '{legal_corp}'),
        StringStruct('LegalTrademarks', '{legal_tm}'),
        StringStruct('OriginalFilename', '{ofn}'),
        StringStruct('ProductName', '{pn}'),
        StringStruct('ProductVersion', '{plain_pv}'),
        StringStruct('Comments', '{comments}')])
      ]), 
    VarFileInfo([VarStruct('Translation', [1033, 1252])])
  ]
)"""

if __name__ == "__main__":
    print(ADMIN_FLAG, TASK_BAR_CLOSE_FLAG, END_TO_PAUSE_FLAG, SAME_NAME_FLAG)
