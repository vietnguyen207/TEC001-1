import random
# Part 1
class Car:
    def __init__(self, regnum, maxsp):
        self.regnum = regnum
        self.maxsp = maxsp
        self.cursp = 0
        self.travdis = 0
    # Part 2
    def accelerate(self, speedchange):
        self.cursp += speedchange
        if self.cursp > self.maxsp:
            self.cursp = self.maxsp
        if self.cursp < 0:
            self.cursp = 0
    # Part 3
    def drive(self, hours):
        self.travdis += (hours*self.cursp)
# Assignment 8
class Race:
    def __init__(self, name, kilometers):
        self.name = name
        self.kilometers = kilometers
        self.car = []
        for i in range (1,11):
            car = Car(f"ABC-{i}", random.randint(150,200))
            self.car.append(car)
    def hour_passes(self):
        for car in self.car:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print(f"{'Reg No':<10} {'Max Speed':<15} {'Current Speed':<20}{'Travelled Distance':<25}")
        print("-" *60)

        for car in self.car:
            print(f"{car.regnum:<10} {car.maxsp:<15} {car.cursp:<20}{car.travdis:<25}")
    def race_finished(self):
        for car in self.car:
            if car.travdis >= self.kilometers:
                return True
        return False
# Part 1
if __name__ == "__main__":
    race = Race("Grand Demolition Derby", 8000)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            print(f"\n Status at {hours} hours")
            race.print_status()
    race.print_status()
    print(f"\nRace finished in {hours} hours!")