import itertools

# бесконечный генератор чисел
gen = itertools.count(0, 2)  # Генерирует числа 0, 2, 4, 6, 8, ...
for i, num in zip(range(10), gen):
    print(num, end=' ')
print('\n')

# применение функции (квадрат числа)
nums = zip([1, 2, 3, 4, 5], [5, 4, 6, 3, 1])
squared_numbers = itertools.starmap(lambda x, y: x ** 2 + y, nums)
print(list(squared_numbers))
print()


# объединение нескольких итераторов
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = itertools.chain(list1, list2, list3)
print(list(combined))
