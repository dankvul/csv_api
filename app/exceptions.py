class ArgumentsError(Exception):
    def __init___(self):
        Exception.__init__(self, "Argument error")


class WrongDataError(Exception):
    def __init___(self):
        Exception.__init__(self, "Wrong data error")
