class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_sound(self, ):
        return self.sound

    def set_sound(self, new_sound):
        self.sound = new_sound


if __name__ == '__main__':
    first_animal = Animal("dog", "woof")
    print(f"Animal name: {first_animal.get_name()}")
    first_animal.set_name("cat")
    print(f"Animal name: {first_animal.get_name()}")
