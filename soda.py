class Soda:
        def __init__(self, add):
                if isinstance(add, str):
                    self.add = add
                else:
                    self.add = None

        def show_my_drink(self):
                if self.add:
                    print(f'Газировка и {self.add}')
                else:
                    print('Обычная гозировка')
a = int(input("Какая газировка нужна?"))
soda = Soda(add = "Крем")
soda2 = Soda(add = None)
if a == 1:
    soda.show_my_drink()
elif a == 2:
    soda2.show_my_drink()
     
