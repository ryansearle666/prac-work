"""client code to Class: Car, Subclass: Taxi"""

from prac_08.taxi import Taxi

def main():
    my_taxi = Taxi("Prius1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)

main()