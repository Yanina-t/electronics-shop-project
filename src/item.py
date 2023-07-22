import csv
from pathlib import Path



class Item:
    """
    Класс для представления товара в магазине.
    """
    ROOT_PATH = Path(__file__).parent
    OPERATION_PATH = Path.joinpath(ROOT_PATH, 'items.csv')
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Магический метод для отображения информации об объекте класса для пользователей
        """
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        """
        Возвращает имя. К атрибуту можно обращаться без ().
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Возвращает имя. К атрибуту можно обращаться без ().
        проверять, что длина наименования товара не больше 10 символов.
        В противном случае обрезать строку (оставить первые 10 символов).
        """
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """
        инициализация экземпляров класса Item данными из файла src/items.csv
        """
        cls.all = []
        with open(cls.OPERATION_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cls(
                        (row['name']),
                        cls.string_to_number(row['price']),
                        cls.string_to_number(row['quantity'])
                    )
                except FileNotFoundError:
                    print("Ошибка, значение не найдено")

    @staticmethod
    def string_to_number(num_str) -> int:
        """
        Возвращает целое число из числа-строки
        :param num_str: Строчное число
        :return: Int число
        """
        return int(float(num_str))

    def __add__(self, other):
        """
        Сложение экземпляров класса Phone и Item (сложение по количеству товара в магазине)
        """
        if isinstance(self.quantity, Item) or (other.quantity, Item) is False:
            return 'Экземпляр не Phone или Item классов'
        return self.quantity + other.quantity
