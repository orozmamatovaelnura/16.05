class Animal:       #  Создаем главный класс животных
  def __init__(self,specie,mass,size,hibernate,migrate):
    self.specie=specie
    self.mass=mass
    self.size=size
    self.hibernate=hibernate
    self.migrate=migrate


class Carnivores(Animal):   #  Наследуем от класса животных плотоядных
  def eat(self):
    self.eating_food='Mostly eat fish , meat , rodents , insects etc.'

class Herbivores(Animal):   #  Наследуем от класса животных травоядных  
  def eat(self):
    self.eating_food='Mostly eat plants , algae , herbs etc.'

class Omnivores(Animal):   #  Наследуем от класса животных всеядных
  def eat(self):
    super().eat()
    self.eating_food='Eat fish , meat , rodents , insects etc. and plants , algae , herbs etc.'

class Birds(Carnivores):   
  blood='warm-blooded'
  is_vertebrate='Birds are vertebrates'
  def can_fly(self):
    self.fly='Birds can fly'

class Penguin(Birds):
  def __init__(self,specie,mass,size,hibernate,migrate,extinct):
    super().__init__(specie,mass,size,hibernate,migrate)
    self.extinct=extinct
  def eat(self):      #   Меняем рацион питания(пингвины-хищники,ф не всеядные,как многие птицы)
    super().eat()
    self.eating_food='Eat fish , krill , squids etc.'   #Рацион пингвинов немного отличается от многих хищников-млекопитающих,к которым мы привыкли
  def can_fly(self):
    super().can_fly()
    self.fly='Penguins can\'t fly'   # Указываем , что пингвины не умеют летать

class Falcon(Birds):
  def __init__(self,specie,mass,size,hibernate,migrate,extinct):
    super().__init__(specie,mass,size,hibernate,migrate)
    self.extinct=extinct
  def eat(self):
    super().eat()
    self.eating_food='Falcons eat rodents , other birds , snakes etc.'
  

class Fish(Carnivores):
  have_gills='Has gills'
  blood='cold-blooded'
  def __init__(self,specie,mass,size,hibernate,migrate,group):
    super().__init__(specie,mass,size,hibernate,migrate)
    self.group=group
  def can_swim(self):
    self.swim='Fish can swim'

class Trout(Fish):
  def __init__(self,specie,mass,size,hibernate,migrate,group,extinct):   #  Добавляем новое значени - значение вымирания
    super().__init__(specie,mass,size,hibernate,migrate,group)
    self.extinct=extinct
  def eat(self):
    super().eat()
    self.eting_food='Trouts eat aquatic insects, terrestrial insects, other fish, crustaceans, leeches, worms, and other foods'

class Mammal(Omnivores,Carnivores,Herbivores):   # Указываем , что млекопитающие бывают разновидными (это никак не помогло,но для понятности можно оставить:))
  is_vertebrate='Mammals are vertebrates'      # Несколько отличительных черт для млекопитающих
  blood='warm-blooded'
  has_mammary_glands='Has mammary glands'
  def __init__(self,specie,mass,size,hibernate,migrate,pregnancy_time):
    super().__init__(specie,mass,size,hibernate,migrate)
    self.gestation_time=pregnancy_time

class Whale(Mammal):
  def __init__(self,specie,mass,size,hibernate,migrate,pregnancy_time,extinct):
    super().__init__(specie,mass,size,hibernate,migrate,pregnancy_time)
    self.extinct=extinct    
  def eat(self):
    super().eat()
    self.eating_food='Eat crabs, octopuses, zooplankton, fish, krill etc.'
  def can_swim(self):     # Из-за того что большинство млекопитающих сухопутные,указываем исключение дл китов
      self.swim='Whales can swim'

sokol=Falcon('Merlin falcon','200 g','30 cm',hibernate=False,migrate=True,extinct=False)
sokol.eat()
sokol.can_fly()
penguin1=Penguin('Emperor penguin','23 kg','1.2 m',hibernate=False,migrate=True,extinct=False)
penguin1.eat()
penguin1.can_fly()
trout1=Trout('Brown trout','9 kg','33 cm',hibernate=False,migrate=True,group='bony fish',extinct=False)
trout1.eat()
trout1.can_swim()
whale1=Whale('Blue whale','200 tonns','30 m',hibernate=False,migrate=True,pregnancy_time='11 months',extinct=True)
whale1.eat()
whale1.can_swim()
print(f'{sokol.specie}\nMass : {sokol.mass}\nSize : {sokol.size}\n{sokol.eating_food}\n{sokol.fly}\nBlood type : {sokol.blood}')
print(f'{sokol.is_vertebrate}\nHibernate : {sokol.hibernate}\nMigrate : {sokol.migrate}\nExtinct : {sokol.extinct}')
print()
print(f'{penguin1.specie}\nMass : {penguin1.mass}\nSize : {penguin1.size}\n{penguin1.eating_food}\n{penguin1.fly}\nBlood type : {penguin1.blood}')
print(f'{penguin1.is_vertebrate}\nHibernate : {penguin1.hibernate}\nMigrate : {penguin1.migrate}\nExtinct : {penguin1.extinct}')
print()
print(f'{trout1.specie}\nMass : {trout1.mass}\nSize : {trout1.size}\nFish group : {trout1.group}\n{trout1.eating_food}\n{trout1.swim}')
print(f'Blood type : {trout1.blood}\n{trout1.have_gills}\nHibernate : {trout1.hibernate}\nMigrate : {trout1.migrate}\nExtinct : {trout1.extinct}\n')
print()
print(f'{whale1.specie}\nMass : {whale1.mass}\nSize : {whale1.size}\nGestation period : {whale1.gestation_time}')
print(f'{whale1.eating_food}\n{whale1.swim}\nBlood type : {whale1.blood}\n{whale1.is_vertebrate}\n{whale1.has_mammary_glands}\nHibernate : {whale1.hibernate}\nMigrate : {whale1.migrate}\nExtinct : {whale1.extinct}')

