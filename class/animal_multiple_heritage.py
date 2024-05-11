class Animal():
    def __init__(self, n_paws, n_eyes,  ) -> None:
        self.n_paws = n_paws
        self.n_eyes = n_eyes


class Mammal(Animal):
    def __init__(self, fur_color, **kw) -> None:
        super().__init__(**kw)
        self.fur_color = fur_color

class Birds(Animal):
    def __init__(self, beak_color, **kw) -> None:
        super().__init__(**kw)
        self.beak_color = beak_color


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class Lion(Mammal):
    pass


class Platyplus(Mammal, Birds):
    pass