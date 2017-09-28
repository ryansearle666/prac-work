""""""

class Guitar:
    """"""
    def __init__(self, name="", year = 0, cost = 0.0):
        """"""
        self.name = name
        self.year = year
        self.cost = cost
        self.current_year = 2017

    def get_age(self):
        """"""
        guitar_age = self.current_year
        self.current_year -= self.year
        return guitar_age

    def is_vintage(self):
        """"""
        if self.get_age() >= 50:
            return True

    def __str__(self):
        """"""
        return "{:15} ({}) : ${:>.2f}".format(self.name, self.year, self.cost)