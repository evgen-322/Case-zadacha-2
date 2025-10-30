# base_derived_demo.py

class Animal:
    """Базовый класс"""
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

    def info(self):
        return f"This is an animal named {self.name}"


class Dog(Animal):
    """Производный класс (наследует от Animal)"""
    
    def __init__(self, name, breed):
        super().__init__(name)  # вызов конструктора базового класса
        self.breed = breed

    def speak(self):
        # Переопределение метода (полиморфизм)
        return "Woof! Woof!"

    def info(self):
        # Расширение функциональности базового метода
        base_info = super().info()
        return f"{base_info}, breed: {self.breed}"


def main():
    # Создание объекта базового класса
    generic_animal = Animal("Unknown")
    print("=== Базовый класс ===")
    print(generic_animal.info())
    print("Sound:", generic_animal.speak())

    print("\n=== Производный класс ===")
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.info())
    print("Sound:", dog.speak())

    print("\n=== Полиморфизм (через общую переменную) ===")
    creatures = [generic_animal, dog]
    for creature in creatures:
        print(f"{creature.name} says: {creature.speak()}")


if __name__ == "__main__":
    main()
