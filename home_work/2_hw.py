def task_1() -> None:
    my_number = 42
    my_float = 3.14
    my_string = "Привет"
    my_list = [1, 2, 3]
    my_bool = True

    print(f"Тип my_number: {type(my_number)}")
    print(f"Тип my_float: {type(my_float)}")
    print(f"Тип my_string: {type(my_string)}")
    print(f"Тип my_list: {type(my_list)}")
    print(f"Тип my_bool: {type(my_bool)}")


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]

    print(f"{a[:3]}")
    print(f"{a[0]}, {a[1]}, {a[2]}")
 #(Эта последовательность чисел называется Числа Фибоначчи)


def task_3(number: int) -> int:
    return number ** 2



print("РЕЗУЛЬТАТ ЗАДАЧИ 1:")

task_1()


print("РЕЗУЛЬТАТ ЗАДАЧИ 2:")

task_2()


print("РЕЗУЛЬТАТ ЗАДАЧИ 3:")

result = task_3(7)
print(f"Квадрат числа 7 = {result}")
print(f"Квадрат числа 5 = {task_3(5)}")
