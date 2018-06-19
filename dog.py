class Dog:
    # the constructor
    def __init__(self, name, month, day, year, speak_text):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speak_text = speak_text

    # accessor
    def speak(self):
        return self.speak_text

    def get_name(self):
        return self.name

    def birth_date(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

    # mutator
    def change_bake(self, bark):
        self.speak_text = bark

    # operator overloading
    # pick the first dog's birthday + 1 year as puppy's birthday
    def __add__(self, other_dog):
        return Dog("Puppy of " + self.name + " and " + other_dog.name,
                   self.month, self.day, self.year + 1, self.speak_text + other_dog.speak_text)


def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birth_date())
    print(girlDog.birth_date())

    boyDog.change_bake("woofywoofy")
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.get_name())
    print(puppy.birth_date())


# The if statement evaluates to True when the program runs as a stand-alone program.
# It evaluates to False when the module is imported into another module.
if __name__ == "__main__":
    main()