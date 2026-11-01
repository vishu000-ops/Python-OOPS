class Chai:
    def __init__(self, type, strength):
        self.type = type
        self.strength = strength

class GingerChai(Chai):
    def __init__(self, type, strength, spice_level):
        super().__init__(type, strength)
        self.spice_level = spice_level