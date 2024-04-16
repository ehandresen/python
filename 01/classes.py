class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def introduce(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

p1 = Person('Eirik', 29)
p2 = Person('Jack', 25)

print(p1)
print(p2)
