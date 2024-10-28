
#Программа для фильтрации элементов списка
import random

#Функция для фильтрации чисел, которые без остатка делятся на m
def filter_numbers(num, m):
  return num % m != 0

#Функция для фильтрации строк
def filter_strings(element):
  return type(element) == str

#Запрос параметров у пользователя
n = int(input("Введите длину списка: "))
operation = int(input("Выберите операцию (1 - отфильтровать числа, 2 - отфильтровать строки): "))
m = 0
if operation == 1:
  m = int(input("Введите параметр m для фильтрации чисел: "))
  #Генерация списка с рандомными элементами
  random_list = [random.choice([random.randint(1, 20)]) for _ in range(n)]
print("Исходный список:", random_list)

#Фильтрация списка
if operation == 1:
  filtered_list = list(filter(lambda x: filter_numbers(x, m), random_list))
else:
  filtered_list = list(filter(filter_strings, random_list))

print("Отфильтрованный список:", filtered_list)