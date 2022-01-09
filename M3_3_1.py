def area(a, b, c):
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


a = int(input("Введите длину стороны А треугольника "))
b = int(input("Введите длину стороны B треугольника "))
c = int(input("Введите длину стороны C треугольника "))

print("Площадь треугольника =", area(a, b, c))
