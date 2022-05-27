class Student:
    
    school="Akrachix"
    def __init__(self,first_name,last_name,age,country):    
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country 
        
    
    # def greet(self):
    #     return f"Hello {self.name} welcome to {self.school}. How is {self.country}"    

    def fullname(self):
        return f"Hello {self.first_name} {self.last_name} welcome to {self.school}. How is {self.country}"
    
    def years_of_birth(self):
        year_of_birth=2022-self.age
        return f"Hello you were born in {year_of_birth}"
    
    def initials(self):
        return f"Hello your initials are {self.first_name[0]}{self.last_name[0]}"
        
        
   