class InvalidBetException(Exception):

    def __init__(self):
        self.message = "please provide a positive integer value"
        super().__init__(self.message)


class InvalidScoreException(Exception):

    def __init__(self):
        self.message = "value should be greater than 0"
        super().__init__(self.message)


class InvalidResponseException(Exception):

    def __init__(self):
        self.message = "please enter an acceptable value"
        super().__init__(self.message)