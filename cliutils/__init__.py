try:
    from cliutils.set_version import run as setVersion
    from cliutils.set_version import set_args_and_run
except (ImportError, ModuleNotFoundError):
    from .set_version import run as setVersion
    from .set_version import set_args_and_run
except (ImportError, ModuleNotFoundError):
    from set_version import run as setVersion
    from set_version import set_args_and_run
