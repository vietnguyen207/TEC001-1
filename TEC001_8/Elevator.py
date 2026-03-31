class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor")        
    def go_to_floor(self, fl):
        if fl > self.top or fl < self.bottom:
            print("This floor does not exist")
        print(f"Moving to floor {fl}")
        while self.current_floor < fl:
            self.floor_up()
        while self.current_floor > fl:
            self.floor_down()
class Building:
    def __init__(self, bottom, top, ele):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(ele):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)
    def run_elevator (self, numele, des):
        if numele < 0 or numele > len(self.elevators):
            print("Invalid number of elevator")
            return
        print(f"Running elevator {numele} to floor {des}")
        self.elevators[numele-1].go_to_floor(des)
    def fire_alarm(self):
        for i, eleva in enumerate(self.elevators):
            print(f"Elevator {i+1} returning to bottom floor")
            eleva.go_to_floor(self.bottom)
if __name__ =="__main__":
    h = Elevator(1,5)
    h.go_to_floor(4)
    h.go_to_floor(1)
    building1 = Building(1,5,3)
    building1.run_elevator(3,4)
    building1.fire_alarm()
