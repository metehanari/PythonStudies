#instance of class example.

class Cat:
    years = 0
    def cat_years(self):
        return self.years * 4
    

effy = Cat()

effy.years = 6

print(effy.cat_years())