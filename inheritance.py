class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, message):
        print(f"speak --> {message}")


class Doctor:
    def __init__(self, name, age, specialty, years):
        self.name = name
        self.age = age
        self.specialty = specialty
        self.years = years

    def speak(self, message):
        print(f"speak --> {message}")

    def cure(self, disease):
        print(f"cure --> {disease}")
