class Product:

    __name: str
    __dscription: str
    __price: float

    def __init__(self, name, description, price):
        self.__name = name
        self.__description = description
        self.__price = price

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_sobrenome(self, description: str):
        self.__description = description

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price):
        self.__price = price


