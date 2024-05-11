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

    def bark(self) -> None:
        print("i'm barking!!!")


class Cat(Mammal):

    def meow(self) -> None:
        print("i'm meowing!!!")



class Lion(Mammal):

    def roar(self) -> None:
        print("i'm roaring!!!")


class Platyplus(Mammal, Birds):

    def grunt(self) -> None:
        print("i'm grunting")

dog = Dog(fur_color="caramel",n_paws=4,n_eyes=2)
print(dog)
dog.bark()

cat = Cat(fur_color="black",n_paws=4,n_eyes=2)
print(cat)
cat.meow()

lion = Lion(fur_color="orange",n_paws=4,n_eyes=2)
print(lion)
lion.roar()

platyplus = Platyplus(fur_color="brown",beak_color="orange",n_paws=4,n_eyes=2)
print(platyplus)
platyplus.grunt()
