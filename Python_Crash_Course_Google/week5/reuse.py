#composition and reuse
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
# polo is an instance of shirt class

sweatpants = pants("Sweatpants")
# sweatpants is an instance of pants class

polo.add_item(polo.name, polo.material, 4)
#add_item method is inherited from Clothing class

sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
#add_item method is inherited from Clothing class

current_stock = polo.Stock_by_Material("Cotton")
#Stock_by_Material method is inherited from Clothing class

print(current_stock)