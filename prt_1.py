
#Программа для фильтрации элементов списка
import random

#Функция для фильтрации чисел, которые без остатка делятся на m
def filter_numbers(num, m):
  return num % m != 0

#Функция для фильтрации строк
def filter_strings(element):
  return type(element) == str
