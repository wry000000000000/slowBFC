try:
    from logger import ConsoleLogger
    from logger.constants import INFO, DEBUG
except ModuleNotFoundError:

    class ConsoleLogger(object):
        def __init__(self, *s):
            pass

        def log(self, i, j):
            print(i, j)

    INFO = 1
    DEBUG = 2


class _version_info(object):
    def __init__(self, major: int, minor: int, micro: int, xmicro: int):
        self._major = major
        self._minor = minor
        self._micro = micro
        self._xmicro = xmicro

    def __tuple__(self) -> tuple:
        return (self.major, self.minor, self.micro, self.xmicro)

    def __list__(self) -> list:
        return list(tuple(self))

    @property
    def major(self) -> int:
        ...
        return self._major

    @property
    def minor(self) -> int:
        ...
        return self._minor

    @property
    def micro(self) -> int:
        ...
        return self._micro

    @property
    def xmicro(self) -> int:
        ...
        return self._xmicro

    @property
    def releaselevel(self) -> object: ...
    @property
    def serial(self) -> int: ...
    def __repr__(self) -> str:
        return f"slowBFC.projectConfigReader.versionInfo({self.major}, {self.minor}, {self.micro}, {self.xmicro})"

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}.{self.xmicro}"

    def __getitem__(self, k: int):
        if type(k) != int:
            return None
        if k > 3:
            return None
        elif k == 0:
            return self.major
        elif k == 1:
            return self.minor
        elif k == 2:
            return self.micro
        elif k == 3:
            return self.xmicro


class ProjectConfigReader(object):
    @property
    def has_settings(self):
        return self.parsed != None

    def has_attr(self, attr: str):
        if not self.parsed:
            return None
        return attr in self.parsed.keys()

    def __init__(self, text: str) -> None:
        self.logger = ConsoleLogger("project_info_parser")

        self.text = text.strip()
        self.parsed = self.parse()

    def __dict__(self) -> dict:
        return self.parsed

    def __bool__(self) -> bool:
        return bool(self.parsed)

    def parse(self) -> dict:
        if (
            not self.text.strip("\n")
            .strip()
            .startswith("REM  QBFC Project Options Begin")
        ):
            return None
        usable_text = str()
        for i in self.text.split("\n"):
            if i == "REM  QBFC Project Options Begin":
                continue
            elif i == "REM  QBFC Project Options End":
                break
            else:
                usable_text += i + "\n"
        _dic = dict()
        embedded_file_list = list()
        for i in usable_text.split("\n"):
            if i.startswith("::  HasVersionInfo: "):
                if i.strip("::  HasVersionInfo: ").strip() == "No":
                    _dic["HasVersionInfo"] = False
                else:
                    _dic["HasVersionInfo"] = True
            elif i.startswith("REM  ShowCloseTaskBar"):
                _dic["ShowCloseTaskBar"] = i.strip().endswith("Yes")
            elif i.startswith("REM  PauseAfterRun"):
                _dic["PauseAfterRun"] = i.strip().endswith("Yes")
            elif i.startswith("REM  UseAdmin"):
                _dic["UseAdmin"] = i.strip().endswith("Yes")
            elif i.strip().startswith("REM  Productversion: ") or i.strip().startswith(
                "REM  Fileversion: "
            ):
                _ = _version_info(
                    *i.strip("REM  Productversion: ")
                    .strip("REM  Fileversion: ")
                    .strip()
                    .split(".")
                )
                if "File" in i:
                    _dic["Fileversion"] = _
                else:
                    _dic["Productversion"] = _
            elif i.strip().startswith("REM  Embeddedfile:"):
                embedded_file_list += [i.strip().lstrip("REM  Embeddedfile:")]
            else:
                if len(i.strip("REM").strip().split(":")) == 1:
                    _dic[i.strip("REM").strip().split(":")[0].strip()] = None
                else:
                    _dic[i.strip("REM").strip().split(":")[0].strip()] = (
                        (":".join(i.strip("REM").strip().split(":")[1:]).strip())
                        if ":".join(i.strip("REM").strip().split(":")[1:])
                        .replace(":", str())
                        .strip()
                        else None
                    )
        # print(_dic)
        self.logger.log(DEBUG, f"嵌入的文件：{embedded_file_list}")
        _dic["Embeddedfiles"] = embedded_file_list
        self.logger.log(DEBUG, f"文件信息：{_dic}")
        return _dic

    def __getitem__(self, item: str):
        if not self.has_attr(item):
            return None
        return self.parsed[item]


if __name__ == "__main__":
    pcr = ProjectConfigReader(
        """
REM  QBFC Project Options Begin
::  HasVersionInfo: No
REM  Companyname: 2
REM  Productname: 
REM  Filedescription: 
REM  Copyrights: 
REM  Trademarks: 
REM  Originalname: 
REM  Comments: 
REM  Productversion:  0. 0. 0. 0
REM  Fileversion:  0. 0. 0. 0
REM  Internalname: 
REM  Appicon: E:\\test.ico
REM  QBFC Project Options End

echo maimaiDX

"""
    )
    print(pcr.parsed)
