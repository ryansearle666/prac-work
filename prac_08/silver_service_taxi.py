""""""

from  prac_08.taxi import Taxi

class Silver_Service_Taxi(Taxi):
    """Specialised version of Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness = 1):
        super.__init__(name, fuel)
        self.fanciness = float(fanciness)

    def get_fare(self):
        """Return the price for the taxi trip."""
        self.price_per_km = Taxi.price_per_km * self.fanciness
        return self.price_per_km * self.current_fare_distance

    def __str__(self):
        return "{}, {}km on current fare, ${.2f}/km plus flagfall of ${.2f}".format(super().)