"""===== Lambda-функция: ======"""
first = 'Мама мыла раму'
second = 'Рамена мало было'
lst = list(map(lambda x, y:  x == y, first, second))

print(lst)


"""===== Замыкание: ====="""
def get_advanced_writer(file_name):         # file_name - параметр, принимающий название файла для записи
    """Функция принимает один параметр имя файла и возвращает функцию write_everything"""
    def write_everything(*data_set):        # *data_set - параметр принимающий неограниченное количество данных любого типа
        """Функция добавляет в файл file_name все данных из data_set в том же виде."""
        with open(file_name, 'w', encoding='utf-8') as file:
            for x in data_set:
                file.writelines(str(x) + '\n')

    return write_everything

write = get_advanced_writer('example1.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


"""===== Метод __call__: ====="""
from random import choice
class MysticBall:
    """Класс принимает в качестве параметра коллекцию строк."""
    def __init__(self, *words):
        """Конструктор класса"""
        self.words = list(words)

    def __call__(self):
        """Метод случайным образом выбирает из списка строк words слово
        и возвращает его"""
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
