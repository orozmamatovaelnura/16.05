#------------1------------
from datetime import date

class Contact:
  def __init__(self,id,first_name,last_name,birth_date,profession):
    self.id=id
    self.first_name=first_name
    self.last_name=last_name
    self.birth_date=birth_date
    self.profession=profession
  def get_information(self):
    print(f'ID - {self.id}')
    print(f'Full name - {self.first_name} {self.last_name}')
    print(f'Birth date - {self.birth_date.day}.{self.birth_date.month}.{self.birth_date.year}')
    print(f'Profession - {self.profession}')
c = Contact(3,'Princilla','Brown',date(day=1, month=12, year=1830),'Witch')

c.get_information()

