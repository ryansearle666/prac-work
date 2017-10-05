""""""


from prac_08.unreliable_car import Unreliable_Car


def main():
    my_unreliable_car = Unreliable_Car("Ford", 100, 65)
    print(my_unreliable_car)
    my_unreliable_car.drive(30)
    print(my_unreliable_car)

main()