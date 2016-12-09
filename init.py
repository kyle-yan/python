class Enemy:

    def __init__(self, x): # 每个对象在调用类的时候都会先执行以下init
        self.energy = x

    def get_energy(self):
        print(self.energy)

enemy5 = Enemy(5)
enemy18 = Enemy(18)

enemy5.get_energy()
enemy18.get_energy()
