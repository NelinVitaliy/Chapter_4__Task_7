class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        print(f'name: {self.name}, age: {self.age}, major: {self.major}')


Steve = Student('Steven Schultz', 23, 'English')
Johnny = Student('Jonathan Rosenberg', 24, 'Biology')
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')

Steve.__str__()
Johnny.__str__()
Penny.__str__()

# print(Steve.__dict__)
# print(Johnny.__dict__)
# print(Penny.__dict__)
