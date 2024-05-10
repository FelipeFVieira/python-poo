class Animal():
    def __init__(self, n_paws, n_eyes,  ) -> None:
        self.n_paws = n_paws
        self.n_eyes = n_eyes


class Mammal(Animal):
    

class Birds(Animal):
    


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class Lion(Mammal):
    pass


class Platyplus(Mammal, Birds):
    pass