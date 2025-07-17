##class Character :
##  def __init__(self, name, weapon) :
##    self.name = name
##    self.weapon = weapon
##    
##  def intro(self) :
##    print("Name : ", self.name)
##    print("Weapon : ", self.weapon)
##
##lugo = Character("Lugo","gun")
##lugo.intro()
##class Action(Character) :
##  step = 0
##
##  def move_forward(self,n) :
##    self.step += n
##    print("Current Location is %d. " % self.step)
##  def move_backward(self,n) :
##    self.step -= n
##    print("Current Location is %d. " % self.step)
##
##  def turn_right(self):
##    print("Turn right.")
##  def turn_left(self):
##    print("Turn left.")
##
##lugo = Action("Jin", "knife")
##
##lugo.move_forward(10);
##lugo.move_backward(3);
##lugo.turn_right()
##lugo.turn_left()

##n = int(input("정수입력 : "))
##j = 0
##for i in range(1,n+1) :
##  if i % 2 == 0 :
##    j = j+1
##print(j)

##n = int(input("정수입력 : "))
##for i in range (1,n+1) :
##  if i%3 == 0 and i%2 == 0 :
##    print (i)


##n = int(input("정수입력 : "))
##for i in range(1,n+1) :
##  if n % i == 0 :
##    print(i)


##n = int(input("정수입력 : "))
##j = 0
##for i in range (1,n+1) :
##  print(i, end = " ")
##  j = j+1
##  if j == 10 :
##    print()
##    j = 0























