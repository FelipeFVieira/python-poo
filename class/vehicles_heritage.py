
### Developing heritage

class vehicles :

    def __init__(self,color,license_plate,n_wheels) -> None:
        self.color = color
        self.license_plate = license_plate
        self.n_wheels = n_wheels

    def start_engine(self) -> str:
        print(f"{self.__class__.__name__} starting engine...")
        print("engine running!")
    
class car(vehicles):
    pass


class motorcycle(vehicles):
    pass

class truck(vehicles):
    pass


### Demonstrating how inheritance works


### Car

car = car("red","abcd-123",4)
print(car)
car.start_engine()

### Motorcycle

motorcycle = motorcycle("lightblue","dcba-321",2)
print(motorcycle)
motorcycle.start_engine()

### Truck

truck = truck("red","abcd-321",8)
print(truck)
truck.start_engine()