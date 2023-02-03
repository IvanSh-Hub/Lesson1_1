
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def isWeekEnd(day):
    if day == 6 or day  == 7:
        print("да")
    else:
        print("нет")

# isWeekEnd(5)



# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

def quarterNumber(x, y):
    if x == 0 or y == 0:
        print("The arguments must be positive")
    else:
        if x > 0 and y > 0:
            print("The point is in the 1 quarter")
        elif x < 0 and y > 0:
            print("The point is in the 2 quarter")
        elif x < 0 and y < 0:
            print("The point is in the 3 quarter")
        else:
            print("The point is in the 4 quarter")

# quarterNumber(-4,0)


#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


class Coordinates():
    def _init_(self):
        pass

    def coords(self, qrt):
        if qrt == 1:
            print("x = [1 to inf], y = [1 to inf]")
        elif qrt == 2:
            print("x = [-1 to -inf], y = [1 to inf]")
        elif qrt == 3:
            print("x = [-1 to -inf], y = [-1 to -inf]")
        else:
            print("x = [1 to inf], y = [-1 to - inf]")

# check = Coordinates()
# check.coords(2)

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09


class Points():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        catX2 = pow(self.x2 - self.x1, 2)
        caty2 = pow(self.y2 - self.y1, 2)
        sum = catX2 + caty2
        return pow(sum, 0.5)


# dist = Points(4,5,10,3)
# d = dist.distance()
# print(d)


# Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def checkPredicate(x, y, z):
    l = not (x or y or z)
    r = not x and not y and not z
    result = l == r

    if result:
        print("The expression is true")
    else:
        print("The expression is false")


# checkPredicate(0,1,0)




