class Car:

    def __init__(self):
        self.current_speed = None
        self.max_speed = None
        self.fuel_level = None

    def accelerate(self, value):

        print("\nACCELERATING")

        for x in range(value):
            if (self.current_speed + value) <= self.max_speed:
                if self.fuel_level != 0:
                    self.current_speed += 1
                    self.fuel_level -= 1
                else:
                    print("\nOut Of Fuel")
                    self.current_speed = 0
                    break
            else:
                self.current_speed = self.max_speed

    def brake(self, value):

        print("\nBRAKING")

        if (self.current_speed - value) >= 0:
            self.current_speed -= value
        else:
            self.current_speed = 0

    def refuel(self, value):

        print("\nREFUELING")

        if (self.fuel_level + value) <= 100:
            self.fuel_level += value
        else:
            self.fuel_level = 100




