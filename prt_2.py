#Запрос параметров у пользователя
n = int(input("Введите длину списка: "))
operation = int(input("Выберите операцию (1 - отфильтровать числа, 2 - отфильтровать строки): "))
m = 0
if operation == 1:
  m = int(input("Введите параметр m для фильтрации чисел: "))
  #Генерация списка с рандомными элементами
  random_list = [random.choice([random.randint(1, 20)]) for _ in range(n)]
print("Исходный список:", random_list)
