try:
    from . import constants
except (ImportError, ModuleNotFoundError):
    from project_config_reader import constants


def create_dict(
    *passes,
    has_version_info=...,
    company_name=...,
    product_name=...,
    file_description=...,
    copyrights=...,
    trademarks=...,
    original_name=...,
    comments=...,
    product_version=...,
    file_version=...,
    internal_name=...,
    appicon=...,
    show_close_task_bar=...,
    pause_after_run=...,
    use_admin=...,
    add_files=...,
):
    return {
        "has_version_info": has_version_info,
        "company_name": company_name,
        "product_name": product_name,
        "file_description": file_description,
        "copyrights": copyrights,
        "trademarks": trademarks,
        "original_name": original_name,
        "comments": comments,
        "product_version": product_version,
        "file_version": file_version,
        "internal_name": internal_name,
        "appicon": appicon,
        "show_close_task_bar": show_close_task_bar,
        "pause_after_run": pause_after_run,
        "use_admin": use_admin,
        "add_files": add_files,
    }


class SaveBacker(object):
    def __init__(self, dick: dict):
        self.dict = dick
        self.form_txt()

    def form_txt(self):
        enbedded_file_text = "\n"
        if self.dict:
            for i in self.dict["add_files"]:
                i: str = i
                if not i:
                    continue
                enbedded_file_text += f"REM  Embeddedfile: {i.strip()}\n"
        self._txt = constants.SAVE_BACK_FORMAT.format(
            has=self.dict["has_version_info"],
            cn=self.dict["company_name"],
            pn=self.dict["product_name"],
            fd=self.dict["file_description"],
            cp=self.dict["copyrights"],
            tmark=self.dict["trademarks"],
            oname=self.dict["original_name"],
            comments=self.dict["comments"],
            pversion=self.dict["product_version"],
            fversion=self.dict["file_version"],
            iname=self.dict["internal_name"],
            icon=self.dict["appicon"],
            sct=self.dict["show_close_task_bar"],
            par=self.dict["pause_after_run"],
            ua=self.dict["use_admin"],
            ef=enbedded_file_text,
        ).lstrip("\n")

    def __str__(self):
        return self._txt

    def __repr__(self):
        return "<SBFC.SaveBacker_object>"

    create_dict = classmethod(create_dict)
