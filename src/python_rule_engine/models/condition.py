
class Condition:
    def __init__(self) -> None:
        self.match = False

    def evaluate(self, obj):
        raise NotImplementedError
