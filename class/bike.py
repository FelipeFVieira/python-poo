class bike: 
    def __init__(self,color,model,year,value,gear) -> None:
        self.color = color
        self.model = model
        self.year = year 
        self.value = value
        self.gear = gear

    def honk(self) -> str:
        print("honking honking...")
    
    def stop(self) -> str:
        print("Bike is stoping...")
        print("Bike is stop!!!")

    def run(self) -> str:
        print("Go runniiiiing...")

    def change_gear(self, n_gear) -> str:
        print(f"The gear is changed to {n_gear}º")
        
        def _up_or_down(n_gear) -> str: 
            if n_gear > self.marcha:
                print(f"Up gear!")
            else: 
                print(f"down gear!")

            self.gear = n_gear

        _up_or_down(n_gear)
        
    # def __str__(self) -> str:
    #     return f"Bike: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}:\n{"\n".join([f"{key} = {value}" for key, value in 
                                              self.__dict__.items()])}"
b1 = bike("red","sport-caloi",2006,1500,1)
b1.honk()
b1.change_gear(0)
b1.run()
b1.stop()

print(b1)