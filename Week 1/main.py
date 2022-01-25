import car_class as c

car1 = c.Car()
car1.current_speed = 5
car1.max_speed = 120
car1.fuel_level = 52

car2 = c.Car()
car2.current_speed = 42
car2.max_speed = 200
car2.fuel_level = 82


def display_objects():
    print(f"\nCar 1 Data:\nCurrent Speed: {car1.current_speed}"
          f"\nMax Speed: {car1.max_speed}\nFuel level: {car1.fuel_level}")
    print(f"Car 2 Data:\nCurrent Speed: {car2.current_speed}"
          f"\nMax Speed: {car2.max_speed}\nFuel level: {car2.fuel_level}")


display_objects()

car1.refuel(50)
display_objects()
