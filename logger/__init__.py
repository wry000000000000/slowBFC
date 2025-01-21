# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.
# 从crivity slicer中复制

import logging, datetime
from typing import Set

try:
    from . import constants
except (ImportError, ModuleNotFoundError):
    from logger import constants


class LogOutput(object):
    def __init__(self):
        self._name = __name__


try:
    from colorlog import ColoredFormatter

    logging_formatter = ColoredFormatter(
        "%(purple)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s - %(white)s%(message)s%(reset)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
except ImportError:  # ModuleNotFoundError was new for 3.6 and we're still on 3.5
    from logging import Formatter

    logging_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")


def prt(lv: str, things: str):
    print(
        f"\033[1;35m{datetime.datetime.now().__str__().split('.')[0]},{int(int(datetime.datetime.now().__str__().split('.')[1])/1000)}\033[0m - \033[0;32m{lv}\033[0m - {things}"
    )


class _Logger(object):
    def __init__(self, *what, **wwwt):
        pass

    def setLevel(*self):
        pass

    def addHandler(*self):
        pass

    critical = warning = info = error = debug = staticmethod(prt)

    def critical(self, t):
        prt("CRITICAL", t)

    def warning(self, t):
        prt("WARNING", t)

    def info(self, t):
        prt("INFO", t)

    def error(self, t):
        prt("ERROR", t)

    def debug(self, t):
        prt("DEBUG", t)


class ConsoleLogger(LogOutput):
    def __init__(
        self, __name: str, enable_debug=constants.ENABLE_DEBUG, once=False
    ) -> None:
        super().__init__()
        self._logger = _Logger("")  # logging.getLogger(__name)  # Create python logger
        self._logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()  # Log to stream
        stream_handler.setFormatter(logging_formatter)
        self._logger.addHandler(stream_handler)
        self._show_once = set()  # type: Set[str]
        self.__name = __name
        self.ed = enable_debug
        self.oce = once

    def log(self, log_type: str, message: str) -> None:
        """Log the message to console

        :param log_type: "e" (error), "i"(info), "d"(debug), "w"(warning) or "c"(critical) (can postfix with "_once")
        :param message: String containing message to be logged
        """
        if self.oce:
            log_type = log_type + constants.SHOW_ONCE
        message = str(message)
        message = f"\033[0;35m[{self.__name}]\033[0m {message}"
        if log_type == "w":  # Warning
            self._logger.warning(message)
        elif log_type == "i":  # Info
            self._logger.info(message)
        elif log_type == "e":  # Error
            self._logger.error(message)
        elif log_type == "d" and self.ed:
            self._logger.debug(message)
        elif log_type == "c":
            self._logger.critical(message)
        elif log_type.endswith("_once"):
            if message not in self._show_once:
                self._show_once.add(message)
                self.log(log_type[0], message)
        else:
            print("Unable to log. Received unknown type %s" % log_type)


if __name__ == "__main__":
    cl = ConsoleLogger(__name__)
    cl.log("w", "test")
