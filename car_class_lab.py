
class Car(object):
  def __init__(self, name="General", model="GM",car_type ="saloon"):
    self.name=name
    self.model=model
    self.car_type=car_type
    self.num_of_doors=self.set_no_of_doors(self.name)
    self.num_of_wheels=self.set_no_of_wheels(self.car_type)
    self.speed = 0
    
  def set_no_of_doors(self,name):
    if name=="Porshe" or name=="Koenigsegg":
      return 2
    else:
      return 4
      
  def set_no_of_wheels(self,car_type):
    if car_type=="trailer":
      return 8
    else:
      return 4

  def is_saloon(self):
    if self.car_type=="saloon":
      return True
    else:
      return False
  
  def set_speed_of_car(self,speed):
    if speed==7:
      self.speed=77
    elif speed==3:
      self.speed=1000

  def drive(self,value):       
    self.other = self.__class__(self.name,self.model,self.car_type)         
    self.other.set_speed_of_car(self.value)         
    return self.other