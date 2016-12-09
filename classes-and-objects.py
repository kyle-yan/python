class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        print(str(self.life) + ' life left')


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
