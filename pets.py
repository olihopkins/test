class Cat:
    def __init__(self, name, age, likes, breed):
        self.name = name
        self.age = age
        self.likes = likes
        self.breed = breed

    def speak(self):
        print(f"Meoowww! My name is {self.name} and I just love {self.likes}!")

poncho = Cat("Poncho", 3, "being a rascal", "Siamese")

poncho.speak()