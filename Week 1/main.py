import Car as c

car1 = c.Car(5, 120, 52)
car2 = c.Car(42, 200, 82)


def display_objects():
    print(f"\nCar 1 Data:\nCurrent Speed: {car1.current_speed}"
          f"\nMax Speed: {car1.max_speed}\nFuel level: {car1.fuel_level}")
    print(f"Car 2 Data:\nCurrent Speed: {car2.current_speed}"
          f"\nMax Speed: {car2.max_speed}\nFuel level: {car2.fuel_level}")


display_objects()

car1.refuel(50)
display_objects()
