"""
    Yet Another Config
    ~~~~~~~~~~
    A simple config manager for Python.
    Author: lrs2187
"""

from enum import Enum
import pickle
import json
import os


class ConfigManager(object):
    """Yet Another Config"""

    class SaveType(Enum):
        """Save types."""

        # save_type, (read_flag, write_flag, encoding), file_extension_name

        PICKLE = pickle, ("rb", "wb", None), "pkl"
        """Using `pickle` library to save and load config."""

        JSON = json, ("r", "w", "utf-8"), "json"
        """Using `json` library to save and load config."""

    def __init__(
        self, file_name: str, save_type: "ConfigManager.SaveType" = None
    ) -> None:
        """
        # Yet Another Config

        args:
        - file_name: `str` the file name of the config file.

        defaults:
        - save_type: `Config.SaveType.JSON`
        """
        if not isinstance(file_name, str):
            raise TypeError("file_name must be str.")
        if save_type is None:
            save_type = ConfigManager.SaveType.JSON
        if "." not in file_name:
            file_name += f".{save_type.value[2]}"

        self._file_name = file_name
        self._save_type = save_type.value[0]
        self._save_flags = save_type.value[1]

        self._data = {}
        self._configs = []

        for item in self.__dir__():
            if item.startswith("_") or item in [
                "SaveType",
                "get",
                "set",
                "load",
                "save",
            ]:
                continue
            self._configs.append(item)

    def __repr__(self) -> str:
        return f"<Config file='{self._file_name}'>"

    def load(self) -> None:
        """Load config."""
        if not os.path.exists(self._file_name):
            with open(
                self._file_name, self._save_flags[1], encoding=self._save_flags[2]
            ) as file:
                self._save_type.dump({}, file)

        with open(
            self._file_name, self._save_flags[0], encoding=self._save_flags[2]
        ) as file:
            tmp = self._save_type.load(file)
            if not isinstance(tmp, dict):
                raise TypeError(f"Exception type: {type(tmp)}")
            for i in tmp:
                setattr(self, i, tmp[i])

    def save(self) -> None:
        """Save config."""
        data = {}
        for config in self._configs:
            data[config] = getattr(self, config)

        with open(
            self._file_name, self._save_flags[1], encoding=self._save_flags[2]
        ) as file:
            self._save_type.dump(data, file)


if __name__ == "__main__":  # TODO：将在下一版本中启用

    class TestingConfig(ConfigManager):
        """Testing Config."""

        first_time_run: bool = True

    config = TestingConfig("testing.json")
    config.load()
    print("first_time_run: ", config.first_time_run)
    config.first_time_run = False
    config.save()
