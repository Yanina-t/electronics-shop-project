from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def number_of_sim(self):
        if self.number_of_sim == 0:
            try:
                return self.number_of_sim
            except ValueError:
                print('Количество физических SIM-карт должно быть целым числом больше нуля.')
