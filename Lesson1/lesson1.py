class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self

    def speak(self):
        # return(f'my name is {self.name}, and I am {self.age} year old')
        print(f'my name is {self.name}, and I am {self.age} year old')


player1 = PlayerCharacter('Marek', 676)
# print(player1.speak())
player1.speak()
