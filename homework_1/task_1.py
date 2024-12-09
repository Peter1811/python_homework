class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self, **kwargs):
        print((kwargs['color'] + ' ' if kwargs.get('color') else '') \
               + f"{kwargs['name']} издает звук: {kwargs['sound']}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "мяу")
        self.color = color

    def makesound(self):
        super().make_sound(name=self.name, sound=self.sound, color=self.color)


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "гав")
        self.color = color

    def makesound(self):
        super().make_sound(name=self.name, sound=self.sound, color=self.color)


cat = Cat(name="Мурка", color="черный")
dog = Dog(name="Бобик", color="рыжий")


cat.makesound()
dog.makesound()
