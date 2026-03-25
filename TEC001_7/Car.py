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
# Part 1
if __name__ == "__main__":
    new_car= Car("ABC-123", 142)
    print(new_car.regnum,"\n",new_car.maxsp,"km/h\n",new_car.cursp,"km/h\n",new_car.travdis,"km")
    # Part 2
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    print("\n",new_car.cursp,"km/h")
    new_car.accelerate(-200)
    print(new_car.cursp,"km/h")
    # Part 4
    carlist = []
    for i in range (1,11):
        car = Car(f"ABC-{i}", random.randint(150,200))
        carlist.append(car)
    Done = False
    while not Done:
        for i in range (0,10):
            carlist[i].drive(1)
            if carlist[i].travdis >= 10000:
                Done = True
                break
            else:
                carlist[i].accelerate(random.randint(-10,15))
            
print(f"{'Reg No':<10} {'Max Speed':<15} {'Current Speed':<20}{"Travelled Distance":<25}")
print("-" *60)

for car in carlist:
    print(f"{car.regnum:<10} {car.maxsp:<15} {car.cursp:<20}{car.travdis:<25}")
        
    