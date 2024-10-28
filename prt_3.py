#Фильтрация списка
if operation == 1:
  filtered_list = list(filter(lambda x: filter_numbers(x, m), random_list))
else:
  filtered_list = list(filter(filter_strings, random_list))

print("Отфильтрованный список:", filtered_list)