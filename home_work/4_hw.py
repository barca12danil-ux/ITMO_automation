class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
print(f"Прямоугольник 1: ширина={rect1.width}, высота={rect1.height}")
print(f"Площадь: {rect1.area()}")
print(f"Периметр: {rect1.perimeter()}\n")

rect2 = Rectangle(7, 3)
print(f"Прямоугольник 2: ширина={rect2.width}, высота={rect2.height}")
print(f"Площадь: {rect2.area()}")
print(f"Периметр: {rect2.perimeter()}\n")

rect3 = Rectangle(4, 4)
print(f"Прямоугольник 3: ширина={rect3.width}, высота={rect3.height}")
print(f"Площадь: {rect3.area()}")
print(f"Периметр: {rect3.perimeter()}\n")


# Задача 2: Класс Math
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        if self.b == 0:
            print("Деление: Ошибка! Деление на ноль")
        else:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")

math1 = Math(10, 5)
math1.addition()
math1.multiplication()
math1.division()
math1.subtraction()

print()
math2 = Math(20, 4)
math2.addition()
math2.multiplication()
math2.division()
math2.subtraction()


# Задача 3: Класс для кнопок сайдбара
class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"

btn_text_box = SidebarButton("Text Box")
btn_check_box = SidebarButton("Check Box")
btn_radio_button = SidebarButton("Radio Button")
btn_web_tables = SidebarButton("Web Tables")
btn_buttons = SidebarButton("Buttons")

buttons = [btn_text_box, btn_check_box, btn_radio_button, btn_web_tables, btn_buttons]

print("Текст кнопок:")
for btn in buttons:
    print(f"  - {btn.text} (тип: {btn.type})")

print("\nКлики по кнопкам:")
for btn in buttons:
    print(f"  {btn.click()}")


# Задача 4 (дополнительная): Класс Car
class Car:
    def __init__(self, color="белый", type="седан", year=2020):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска установлен: {self.year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля установлен: {self.type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")

car1 = Car("красный", "спорткар", 2022)
print(f"Автомобиль 1: {car1.color}, {car1.type}, {car1.year}")
car1.start_engine()
car1.stop_engine()

print()
car2 = Car()
car2.set_color("синий")
car2.set_type("внедорожник")
car2.set_year(2021)
print(f"Автомобиль 2: {car2.color}, {car2.type}, {car2.year}")
car2.start_engine()
