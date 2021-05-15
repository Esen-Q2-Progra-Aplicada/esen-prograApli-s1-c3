class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, message):
        print(f"speak --> {message}")


class Doctor(Person):
    def __init__(self, name, age, specialty, years):
        Person.__init__(self, name, age)
        self.specialty = specialty
        self.years = years

    def cure(self, disease):
        print(f"cure --> {disease}")


# ejericico crear una clase Developer, name age, language, years
# debe tener un metodo program -> web app, desktop app, restful api, mobile app
# program --> {app}


class Developer(Person):
    def __init__(self, name, age, language, years):
        super().__init__(name, age)
        self.language = language
        self.years = years

    def program(self, app):
        print(f"program -> {app}")


doctor = Doctor("bal", 23, "heart", 5)
print(doctor.name)
print(doctor.specialty)
doctor.speak("how do you feel?")
doctor.cure("heart attack")
print("")

developer = Developer("dan", 26, "python", "4")
print(developer.name)
print(developer.language)
developer.speak("what are the specs in your machine?")
developer.program("web app")

personList = [doctor, developer]

for pepito in personList:
    print(pepito.name)
