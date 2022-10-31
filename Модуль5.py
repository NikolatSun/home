

class StringVar:
    def __init__(self):
         self.s = ''
    def set (self, val):
        self.s = val
    def get (self):
        return self.s
s = StringVar()
print(s.set('Hallooy'))
print(s.get())






class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1_x = int(input("p1.x: "))
p1_y = int(input("p1.y: "))

p2_x = int(input("p2.x: "))
p2_y = int(input("p2.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

print(p1.dist(p2))






import random
 
class Warrer:
  def __init__(self, name, health=100):
    self.name = name
    self.health = health
    print ('Создан воин {} со здоровьем {}'.format(self.name, self.health))
 
  def strike(self, enemyWarrer):
    if True:
      print('Воин {} нанес урон -20 воину {}'.format(self.name, enemyWarrer.name))
      enemyWarrer.setHealth(
        enemyWarrer.getHealth() - 20
      )
    else:
      print('Некореектно заданно здоровье для воина {}'.format(enemyWarrer.name))
      print(type(enemyWarrer.getHealth()))
 
  def setHealth(self, health):
    self.health = health
    print('Установленно здоровье {} для воина {}'.format(self.health, self.name))
 
  def getHealth(self):
    try:
      return self.health
      print('Здоровье воина {} — {}'.format(self.name, self.health))
    except:
      return 'Здоровье не заданно'
      print('Здоровье для воина {} не заданно'.format(self.name))
 
 
 
one = Warrer('Николай', 100)
two = Warrer('Паша', 100)
 
while (one.health > 0) and (two.health > 0):
  round = random.randint(1, 2)
 
  if round == 1:
    one.strike(two)
  elif round == 2:
    two.strike(one)
 
if round == 1:
  name = one.name
  enemy_name = two.name
elif round == 2:
  name = two.name
  enemy_name = one.name
 
print('Поздравляем воина {}! Он одержал победу над воином {}'.format(name, enemy_name))

