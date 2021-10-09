class TriangleChecker: 
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c 
     
    def is_triangle(self): 
        if self.a <= 0 or self.b <= 0 or self.c <= 0: 
            print("С отрицательными числами ничего не выйдет!") 
        else: 
            sides = sorted((self.a, self.b, self.c), key = lambda x : -x) 
            print("Ура, можно построить треугольник!") if sides[0] < sides[1] + sides[2] else print("Жаль, но из этого треугольник не сделать.")
a=int(input("Проверить треугольник"))
tri1 = TriangleChecker(-1, 4, 5) 
tri2 = TriangleChecker(17, 2, 2)
tri3 = TriangleChecker(6, 7, 8)  
if a==1:
    tri1.is_triangle()
 
elif a==2:
    tri2.is_triangle()
 
elif a==3:
    tri3.is_triangle()
