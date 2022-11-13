from abc import abstractmethod


class Clothes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def calc(self):
        pass

    @property
    def calc(self):
        if self.name == "Coat":
            total = self.size / 6.5 + 0.5
        else:
            total = 2 * self.size + 0.3
        return total


coat = Clothes("Coat", int(input("Укажите необходимое количество пальто: ")))
costume = Clothes("Costume", int(input("Укажите необходимое количество костюмов: ")))

print(f"Расход ткани на пальто: {round(coat.calc, 2)}")
print(f"Расход ткани на костюм: {costume.calc}")
print(f"Общий расход ткани: {round((coat.calc + costume.calc), 2)}")
