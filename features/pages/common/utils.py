import os

# FIXME Need better way to have global variable


class GlobalVar(object):

    log_root_dir = ''
    log_dir = ''

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def take_screenshot(driver):
    if not GlobalVar().log_dir:
        raise SystemError('log_dir is not set.')
    import datetime as dt
    img_path = os.path.join(GlobalVar().log_dir, dt.datetime.now().strftime('%y%m%d-%H%M%S') + '.png')
    driver.get_screenshot_as_file(img_path)
