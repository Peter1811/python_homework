def main():
    # если файл не найден, так и так будет выведено исключение FileNotFoundError
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            # так как задание плохо сформулировано, непонятно, 
            # имеется в виду строка, состоящая ТОЛЬКО из цифр
            # или имеющая цифры
            # мною был выбран первый вариант
            if line.isdigit():
                data.append(line)

    if len(data) == 0:
        # если вообще нет значений, состоящих из чисел
        raise TypeError('нет числовых значений в файле')
    
    else:
        for line in data:
            print(data)
    
main()