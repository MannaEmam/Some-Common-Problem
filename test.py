class Warehouse:
   purpose = 'storage'
   region = 'west'
   def __init__(self):
       self.x = 123

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
w2.x = 789
print(w2.purpose, w2.region, w2.x)
