class Buffer:
    def __init__(self):
        self.memory = []

    def add_data(self, data):
        print(f'пробую добавить {data}')
        if len(self.memory) >= 5:
            print('буффер переполнен, очищаю')
            self.memory.clear()

        else:
            self.memory.append(data)
            print(f'добавлено {data}')

    def get_data(self):
        if len(self.memory) == 0:
            print('буффер пуст')
        else:
            for obj in self.memory:
                print(obj, end=' ')
            print()

buffer = Buffer()
buffer.add_data(1)
buffer.add_data(1)
buffer.add_data(1)
buffer.add_data(1)
buffer.add_data(1)
buffer.get_data()

buffer.add_data(2)

buffer.get_data()
