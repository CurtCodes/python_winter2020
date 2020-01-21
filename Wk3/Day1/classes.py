class wheel:
    def __init__(self, diameter, wtype="All Weather"):
        self.size = diameter
        self.type = wtype

class engine:
    def __init__(self,horsepower,n_cyl):
        self.horsepower = horsepower
        self.n_cyl = n_cyl
        self.is_healthy = True
        self.need_oil_change = False
        self.trip_counter = 0
        self.mileage = 0
        self.max_mileage = 150000

    def check_health(self):
        if self.mileage > self.max_mileage:
            self.is_healthy = False
            self.need_oil_change=True
            print("Our engine is Dusty")

        if self.trip_counter >= 3000:
            self.is_healthy = False
            self.need_oil_change = True
            if self.trip_counter>=15000:
                print("Im dead, thanks")
            elif self.trip_counter>=6000:
                print("Im going to die if you dont change the oil")
            else:
                print("Boop!")
        
            print("Change your oil!")

    
    def change_oil(self):
        print("Thank you for changing oil")
        self.trip_counter = 0
        self.need_oil_change = False
        self.is_healthy = True


class body:
    def __init__(self, color, num_doors=4):
        self.num_doors = num_doors
        self.color = color

        if self.num_doors==0:
            self.trunk_size="tiny"
        elif self.num_doors==2:
            self.trunk_size ="small"
        elif self.num_doors == 4:
            self.trunk_size = "med"
        elif self.num_doors == 5:
            self.trunk_size="large"

        
            