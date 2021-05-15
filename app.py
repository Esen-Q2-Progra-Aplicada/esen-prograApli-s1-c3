class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    # este metodo no retorna valor y no tiene parametros
    def createPerson(self):
        print("created the person...")

    # este metodo no retorna valor y tiene N parametros (en este caso N=1)
    def createPersonWithName(self, name):
        print(f"created the person with name: {name}")

    # este metodo retorna una cadena y no tiene parametros
    def createPersonSendMessage(self):
        message = "created the person...!?"
        return message

    # este metodo retorna una cadena y tiene N parametros (en este caso N=2)
    def createPersonWithNameAgeSendMessage(self, name, age):
        message = f"created the person with name: {name} and age: {age}"
        return message


person = Person(1, "ted", 23)
print(person.name)
print(person.age)

person.createPerson()
person.createPersonWithName("bill")
message = person.createPersonSendMessage()
print(message)
message = person.createPersonWithNameAgeSendMessage("rod", 42)
print(message)
