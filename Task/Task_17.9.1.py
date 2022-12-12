# Напишите программу, которой на вход подается последовательность чисел через пробел, а также
# запрашивается у пользователя любое число. В качестве задания повышенного уровня сложности можете выполнить
# проверку соответствия указанному в условии ввода данных. Далее программа работает по следующему алгоритму:
# 1.Преобразование введённой последовательности в список
# 2.Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# 3.Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним
# больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен
# в этом модуле.Реализуйте его также отдельной функцией.

# Решение

while True:
    try:
        userInput = [int(i) for i in input("Введите последовательность положительных чисел через пробел: ").split()]
        userInput_2 = int(input("Введите любое число из диапазона введёной последовательности: "))
    except ValueError:
        print("Введены неверные значения")
        continue
    else:
        break


def sort():
    for i in range(1, len(userInput)):
        x = userInput[i]
        idx = i
        while idx > 0 and userInput[idx - 1] > x:
            userInput[idx] = userInput[idx - 1]
            idx -= 1
        userInput[idx] = x
    return userInput


def binary_search(userInput, userInput_2, left, right):
    middle = (left + right) // 2
    if userInput[0] >= userInput_2 or userInput_2 > userInput[-1]:
        return f"Введенное число не удовлетворяет условию"
    else:
        if left > right:
            return f"Номер позиции элемента, который меньше введенного числа: {middle}\n" \
                   f"Номер позиции элемента, который больше или равен введенному числу: {middle + 1}"
        elif userInput[middle] == userInput_2:
            return f"Номер позиции элемента, который меньше введенного числа: {middle - 1}\n" \
                   f"Номер позиции элемента, который больше или равен введенному числу: {middle + 1}"
        elif userInput_2 < userInput[middle]:
            return binary_search(userInput, userInput_2, left, middle - 1)
        else:
            return binary_search(userInput, userInput_2, middle + 1, right)


print(f"Отсортированный список: {sort()}")
print(binary_search(userInput, userInput_2, 0, len(userInput)))
