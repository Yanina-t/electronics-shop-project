from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, num_sim: int):
        super().__init__(name, price, quantity)
        if num_sim > 0 and isinstance(num_sim, int):
            self.__num_sim = num_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


    def __repr__(self):
        """
        Магический метод для отображения информации об
        объекте класса в режиме отладки (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__num_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает имя. К атрибуту можно обращаться без ().
        """
        return self.__num_sim

    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        """
        Количество физических SIM-карт должно быть целым числом больше нуля.
        """
        if num_sim > 0 and isinstance(num_sim, int):
            self.__num_sim = num_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
