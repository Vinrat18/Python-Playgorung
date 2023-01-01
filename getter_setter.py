# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

human.temperature = -300


class Celsius:
    def __init__(self) -> None:
        self._temperature = 273

    @property
    def temperature(self):
        print("Getter")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setter")
        self._temperature = value

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32


# create an object
human = Celsius()
human.temperature = 37
print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius()
