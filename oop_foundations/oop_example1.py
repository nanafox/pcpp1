class Duck:
    counter = 0
    species = "duck"

    def __init__(self, height: float, weight: float, sex: str):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    @staticmethod
    def quack():
        print("Quack")


class Chicken:
    species = "chicken"

    def walk(self):
        pass

    @staticmethod
    def cluck():
        print("clucks")


duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)

my_poultry = [duckling, drake, hen, chicken]

print(f"Number of Ducks: {Duck.counter}")

for poultry in my_poultry:
    print(poultry.species, end=" ")
    if poultry.species == "duck":
        poultry.quack()
    elif poultry.species == "chicken":
        poultry.cluck()
