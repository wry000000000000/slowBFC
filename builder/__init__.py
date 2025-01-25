try:
    from . import constants, utils
except (ImportError, ModuleNotFoundError):
    try:
        from builder import constants, utils
    except (ImportError, ModuleNotFoundError):
        import constants, utils
try:
    from logger import ConsoleLogger
    from logger.constants import DEBUG, INFO
except:
    pass
import subprocess, threading, os, base64, sys
from PySide6 import QtWidgets

TEMP = sys._MEIPASS if hasattr(sys, "_MEIPASS") else ".\\tmp"


class Builder(object):
    _set_non_block_read = staticmethod(utils._set_non_block_read)

    @staticmethod
    def _path_sep(path: str) -> list:
        a1 = path.split(os.path.sep)
        l1 = list()
        for i in a1:
            l1 += i.split("/")
        return l1

    def __init__(
        self,
        code: str,
        logger=None,
        TEMPDIR="tmp",
        with_pause: bool = False,
        with_admin=False,
        is_silent=False,
        show_taskbar_icon=False,
        icon_base64=constants.DEFAULT_ICON,
        exe_name="slowBFC_test",
        debug=False,
        add_file_path=None,
        needs_update=False,
        update_window=None,
    ):
        self.add_file_path = add_file_path
        self.update_window = update_window
        code = code.replace("\\", "\\\\").replace("'''", "\\'\\'\\'")  # 防止意外注入
        self.icon_base64 = icon_base64 = (
            icon_base64 if icon_base64 else constants.DEFAULT_ICON
        )
        self.needs_update = needs_update
        if logger == None:
            try:
                logger = ConsoleLogger("exe_builder")
            except NameError:
                pass
        if is_silent:
            with_pause = False  # 否则会弹出空框提示按任意键
        self.is_silent = is_silent
        if not show_taskbar_icon:
            _str = constants.NORMAL_EXECUTE_PY.format(
                code=code,
                pause_code="os.system('pause')" if with_pause else str(),
                admin_code=constants.ADMIN_CODE if with_admin else str(),
                set_file_code=(
                    constants.SET_MY_FILES_VAR_CODE
                    if add_file_path and self.check_walk_has_file()
                    else str()
                ),
            )
        else:
            _str = constants.SHOW_TASKBAR_CODE.format(
                admin_code=constants.ADMIN_CODE if with_admin else str(),
                code=code,
                pause_cmd="&& pause" if with_pause else str(),
                icon_base64=icon_base64,
                exe_name=exe_name,
                no_debug_code1="#" if not debug else str(),
                no_debug_code2="#" if not debug else str(),
                set_file_code=(
                    constants.SET_MY_FILES_VAR_CODE
                    if add_file_path and self.check_walk_has_file()
                    else str()
                ),
            )
        if logger:
            logger.log(DEBUG, f"building str:{_str}")
        else:
            print(_str)
        self._str = _str
        self.ret = None
        self.TEMPDIR = TEMPDIR
        self.logger = logger

    def check_walk_has_file(self):
        if not self.add_file_path:
            return False
        _w = [i for i in os.walk(self.add_file_path)]
        print(self.add_file_path)
        if not _w:
            return False
        if len(_w) > 1:
            return True
        elif len(_w[0]) > 3:
            return True
        elif len(_w[0]) == 2:
            if not _w[0][1]:
                return False
            else:
                return True
        elif len(_w[0]) == 3:
            if (not _w[0][1]) and (not _w[0][2]):
                return False
            else:
                return True
        return False

    def start_build(self, build_finished_event: "function" = lambda emm: emm):
        with open(os.path.join(TEMP, "icon__.ico"), "wb+") as f:
            f.write(base64.b64decode(self.icon_base64))
        self.add_file_path = os.path.abspath(self.add_file_path)
        if self.logger:
            self.logger.log(
                "d", f"path:{self.add_file_path},has_file:{self.check_walk_has_file()}"
            )
        else:
            print(f"path:{self.add_file_path},has_file:{self.check_walk_has_file()}")
        add_data = (
            f"--add-data {self.add_file_path};./my_files/"
            if self.check_walk_has_file()
            else str()
        )
        if self.logger:
            self.logger.log("d", add_data)
        else:
            print(add_data)
        open(f"{self.TEMPDIR}/tmp.py", "w+", encoding="utf-8").write(self._str)
        self._dir = os.getcwd()
        _ip = os.path.abspath(os.path.join(TEMP, "icon__.ico"))
        os.chdir(self.TEMPDIR)
        _this_file_dir = (
            "\\".join(self._path_sep(sys.executable)[:-1])
            if not constants.IS_DEV
            else self._dir
        )
        print(
            f"{_this_file_dir}\\inside_py\\python -m PyInstaller -F tmp.py {'--icon '+_ip} {'-w'if self.is_silent else str()} {add_data}"
        )
        if os.path.exists(os.path.join(self.TEMPDIR, "dist", "tmp.exe")):
            os.remove(os.path.join(self.TEMPDIR, "dist", "tmp.exe"))
        o = subprocess.Popen(
            f"{_this_file_dir}\\inside_py\\python -m PyInstaller -F tmp.py {'--icon '+_ip} {'-w'if self.is_silent else str()} {add_data}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        s = threading.Thread(target=self.buildd)
        self.p = o
        self.bfe = build_finished_event
        s.run()

    def buildd(self):
        while True:
            if self.needs_update:
                self.update_window.update()
                QtWidgets.QApplication.processEvents()
            self.p.stderr.flush()
            line = self.p.stderr.readline()
            if not line:
                self.p.stdout.flush()
                line = self.p.stdout.readline()
            if not line:
                continue
            if line:
                print(">>>>>>", line.decode("GBK"))
                if "Building EXE" in line.decode(
                    "GBK"
                ) and "successfully." in line.decode("GBK"):
                    break
                elif "error" in line.decode("GBK").lower():
                    self.bfe("err")
                    print("err")
                    self.ret = "err"
                    return 0

        print("look up!!! EXIT ===")  # 跳出
        os.chdir(self._dir)
        if os.path.exists(os.path.join(self.TEMPDIR, "build")):
            try:
                os.remove(os.path.join(self.TEMPDIR, "build"))
                if self.logger:
                    self.logger.log(
                        DEBUG, f"已删除临时目录:{os.path.join(self.TEMPDIR, 'build')}"
                    )
                else:
                    print(f"已删除临时目录：{os.path.join(self.TEMPDIR, 'build')}")
            except PermissionError:
                pass
        self.ret = os.path.join(self.TEMPDIR, "dist", "tmp.exe")
        self.bfe(self.ret)


if __name__ == "__main__":
    b = Builder("echo test\necho nm\n %0", show_taskbar_icon=True, debug=False)
    b.start_build()
    while not b.ret:
        import time

        time.sleep(0.1)
    if b.ret == "err":
        exit.__call__()
    print(f'explorer /select,"{b.ret}"')
    os.system(f'explorer /select,"{b.ret}"')
