class CharField:
    def __init__(self, max_length, **kwargs):
        self.max_length = max_length
        self.__dict__.update(kwargs)
