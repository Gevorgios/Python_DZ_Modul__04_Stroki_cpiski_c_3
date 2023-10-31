import random


list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [random.randint(1, 10) for _ in range(10)]


union_list = list1 + list2


unique_list = list(set(union_list))


intersection_list = list(set(list1) & set(list2))


unique_elements_list = list(set(list1) ^ set(list2))


min_max_list = [min(list1), max(list1), min(list2), max(list2)]


print("Список 1:", list1)
print("Список 2:", list2)
print("Третий список, содержащий элементы обоих списков:", union_list)
print("Третий список, содержащий элементы обоих списков без повторений:", unique_list)
print("Третий список, содержащий элементы общие для двух списков:", intersection_list)
print("Третий список, содержащий только уникальные элементы каждого из списков:", unique_elements_list)
print("Третий список, содержащий только минимальное и максимальное значение каждого из списков:", min_max_list)