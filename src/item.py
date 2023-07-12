import csv
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

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
    def open_csv(cls):
        """
        Путь файла items.csv для открытия
        """
        ROOT_PATH = Path(__file__).parent
        OPERATION_PATH = Path.joinpath(ROOT_PATH, 'items.csv')
        return OPERATION_PATH

    @classmethod
    def instantiate_from_csv(cls):
        """
        инициализация экземпляров класса Item данными из файла src/items.csv
        """
        cls.all = []
        file_cls = cls.open_csv()
        with open(file_cls) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cls(
                        row['name'],
                        row['price'],
                        row['quantity']
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
        if "." in num_str:
            str_to_float: float = float(num_str)
            str_to_int: int = int(str_to_float)
        else:
            str_to_int: int = int(num_str)
        return str_to_int
