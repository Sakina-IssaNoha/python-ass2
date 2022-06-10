from turtle import speed


class Vehicle:
    color="White"
    def __init__(self,name,max_speed,mileage):
     self.name=name
     self.max_speed=max_speed
     self.mileage=mileage
     
     
    def congrats(self):
        return f"Congratulations for buying the {self.name},{self.color},{self.max_speed} and {self.mileage}"
    
    def seats(self,capacity):
        return f"{self.name} carries at most {capacity} people" 