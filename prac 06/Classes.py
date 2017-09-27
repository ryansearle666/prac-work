class LegalAgeCheck:
    def __init__(self, first_name="", last_name="", is_legal_age=False):
        self.first_name = first_name
        self.last_name = last_name
        self.is_legal_age = is_legal_age

    def __str__(self):
        return "{} {}, you {} been permitted entry".format(self.first_name, self.last_name, "have" if self.is_legal_age else "have not")

blank = LegalAgeCheck()
print(blank)
summary = LegalAgeCheck("Ryan", "Searle", True)
print(summary)
