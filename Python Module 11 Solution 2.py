class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance_traveled += self.speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # kWh


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # liters


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(140)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car {electric_car.registration_number}:")
print(f"  Distance traveled: {electric_car.distance_traveled} km")
print(f"  Battery capacity: {electric_car.battery_capacity} kWh")

print(f"\nGasoline car {gasoline_car.registration_number}:")
print(f"  Distance traveled: {gasoline_car.distance_traveled} km")
print(f"  Tank volume: {gasoline_car.tank_volume} liters")