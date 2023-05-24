import random
class PasswordGenerator:
    def __init__(self , length , characters):
        self.length = length
        self.characters = characters
    def generate_password(self):
        password = ''
        for i in range(self.length):
            password += random.choice(self.characters)
        return password
rezult = PasswordGenerator(8 , 'vbe%^#@(HBFE4536')
for i in range(3):
    print(f"Пароль: {rezult.generate_password()}")