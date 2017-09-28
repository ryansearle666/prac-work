"""CP1404 Practical: Classes"""


class ProgrammingLanguage:
    """"""

    def __init__(self, field="", typing="", reflection=False, year = 0):
        """"""

        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """"""

        if self.typing == "Dynamic":
            return True

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection, self.year)


