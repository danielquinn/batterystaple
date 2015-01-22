class Colour:
    """
    Courtesy of:
      http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def info(cls, string):
        return cls._wrap(string, cls.OKBLUE)

    @classmethod
    def success(cls, string):
        return cls._wrap(string, cls.OKGREEN)

    @classmethod
    def warning(cls, string):
        return cls._wrap(string, cls.WARNING)

    @classmethod
    def danger(cls, string):
        return cls._wrap(string, cls.FAIL)

    @classmethod
    def _wrap(cls, string, colour):
        return colour + string + cls.ENDC
