class Player :

    def __init__(self,name,age,rank):
        self.name = name
        self.age = age
        self.rank = rank

    def Pass(self):
        print(self.name," passing")

    def Shoot(self):
        print(self.name," Shooting")

    def Jump(self):
        print(self.name," Jumping")

player1 = Player("Bingoo" , 20 , 99)
print(player1.age)
player1.Shoot()  