
### Simple heritage

### Developing heritage 

class vehicles :

    def __init__(self, color: str, license_plate: str, n_wheels: int) -> None:
        self.color = color
        self.license_plate = license_plate
        self.n_wheels = n_wheels

    def start_engine(self) -> str:
        print(f"\n{self.__class__.__name__} starting engine...")
        print("engine running!")

    def __str__(self) -> str:
        
        return f" \n#### {self.__class__.__name__} ####\n{"\n".join([f"{key}: {value} " for key, value 
                                         in self.__dict__.items()])}"
        
    
class car(vehicles):
    pass


class motorcycle(vehicles):
    pass

class truck(vehicles):

    def __init__(self, color: str, license_plate: str, n_wheels: int, loaded: bool) -> None:
        super().__init__(color, license_plate, n_wheels) 
        self.loaded = loaded

    def is_it_loaded(self) -> str:
        print(f"The truck {"is" if self.loaded == True else "is not"} loaded!")

### Demonstrating how inheritance works


### Car

car = car("red","abcd-123",4)
print(car)
car.start_engine()

### Instantiating other vehicles

### Motorcycle

motorcycle = motorcycle("lightblue","dcba-321",2)
print(motorcycle)
motorcycle.start_engine()

### Truck

truck = truck("red","abcd-321",8,False)
print(truck)
truck.is_it_loaded()
truck.start_engine()