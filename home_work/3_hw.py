#Задача 2
def task_2(num1: int, num2: int) -> None:
    if num1 > num2:
        print(f"Наибольшее число: {num1}")
    else:
        print(f"Наибольшее число: {num2}")
task_2(10, 25)
task_2(100, 50)


#Задача 3
def task_3(num1: int, num2: int) -> None:
    if abs(num1 - num2) == 135:
        print("yes")
    else:
        print("No")
task_3(200, 65)
task_3(100, 50)

#Задача 4
def task_4(month: int) -> None:
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Неверный номер месяца")
task_4(1)
task_4(4)
task_4(7)
task_4(10)

#Задача5
def task_5(num1: int, num2: int, num3: int) -> None:
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")
task_5(15, 20, 25)
task_5(5, 20, 25)

#Задача6
def task_6(numbers: list) -> None:
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    print(f"Количество положительных чисел: {count}")
task_6([1, -5, 10, -3, 8])
task_6([-1, -2, -3, -4, -5])

#Задача7
def task_7(years: int, months: int) -> None:
    total_days = years * 365 + months * 29
    print(f"Количество дней: {total_days}")
task_7(2, 3)
task_7(1, 6)
