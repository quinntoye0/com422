class Car:

    def __init__(self, current_speed, max_speed, fuel_level):
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def acc(self, inc_val):

        print("\nACCELERATING")

        if (self.current_speed + inc_val) <= self.max_speed:
            for x in range(inc_val):
                if self.fuel_level != 0:
                    self.current_speed += 1
                    self.fuel_level -= 1
                else:
                    print("\nOut Of Fuel")
                    self.current_speed = 0
                    break
        else:
            self.current_speed = self.max_speed

    def brake(self, dec_val):

        print("\nBRAKING")

        if (self.current_speed - dec_val) >= 0:
            self.current_speed -= dec_val
        else:
            self.current_speed = 0

    def refuel(self, refuel_val):

        print("\nREFUELING")

        if (self.fuel_level + refuel_val) <= 100:
            self.fuel_level += refuel_val
        else:
            self.fuel_level = 100




