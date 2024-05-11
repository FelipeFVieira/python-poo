class Animal():
    def __init__(self, n_paws, n_eyes,  ) -> None:
        self.n_paws = n_paws
        self.n_eyes = n_eyes

    def __str__(self) -> str:
        
        return f" \n#### {self.__class__.__name__} ####\n{"\n".join([f"{key}: {value} " for key, value 
                                         in self.__dict__.items()])}"

class Mammal(Animal):
    def __init__(self, fur_color, **kw) -> None:
        super().__init__(**kw)
        self.fur_color = fur_color

class Birds(Animal):
    def __init__(self, beak_color, **kw) -> None:
        super().__init__(**kw)
        self.beak_color = beak_color


class Dog(Mammal):
    def bark(self):
        print("i'm barking!!!")


class Cat(Mammal):
    pass


class Lion(Mammal):
    pass


class Platyplus(Mammal, Birds):
    pass

