import random
class Enemy:

      def __init__(self,atkl,atkh):
          self.atkl=atkl
          self.atkh=atkh 
      #atkl=60
      #atkh=80
      def getatk(self):
          print(self.atkh)
enemy1 = Enemy(78, 98)
enemy1.getatk()

enemy2 = Enemy(40, 30)
enemy2.getatk()

           


'''
playerhp=260
enemyatk=60
enemyath=80
while playerhp>0:
    dmg=random.randrange(enemyatk,enemyath)
    playerhp=playerhp-dmg
    
    print("Enemy strikes",dmg,"hp points, and Now Player current hp is",playerhp)
    if (playerhp<=0):
       print("Game over. You died")'''
