from uuid import uuid4
from collections import defaultdict
import weakref


HOUSE_TYPE_ENUM = {
    '1': 'Школа',
    '2': 'Десткий Сад',
    '3': 'Институт',
    '4': 'Офис',
}


class AbstractBuilding:
    def __init__(self, house_number: int, house_type: str):
        self.house_number = house_number
        self.house_type = house_type
        self.is_build = False
        self.color = None
        self.quantity_floor = 0
        self.unique_code = uuid4().hex

    def _build_house(self):
        self.is_build = True
        return (
            f'Построено здание {self.house_number} с типом {self.house_type}'
        )


class Building(AbstractBuilding):
    __refs__ = defaultdict(list)

    def __init__(self, house_number: int, house_type: str):
        super().__init__(house_number, house_type)
        self.__refs__[self.__class__].append(weakref.ref(self))

    def set_color(self, color: str):
        self.color = color

    def set_quantity_floor(self, quantity_floor: int):
        self.quantity_floor = quantity_floor

    def build_house(self):
        if self.color and self.quantity_floor != 0:
            super()._build_house()
            return 'Здание построено!'
        else:
            return 'Здание не может быть построено!'

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

    @classmethod
    def build_all(cls):
        for item in cls.get_instances():
            item.build_house()

    def __str__(self):
        return (
            f'Уникальный код - {self.unique_code} \n'
            f'Номер дома - {self.house_number} \n'
            f'Тип дома - {self.house_type} \n'
        )


class City:
    def __init__(self, city_name):
        self.city_name = city_name
        self.houses = {}

    def add_addr(self, building_object):
        if building_object.is_build:
            self.houses[building_object.unique_code] = building_object
            return (
                f'Здание {building_object.house_number} - '
                f'{building_object.house_type} добавлено в список адресов '
                f'города!'
            )
        return 'Нельзя добавить не постороенное здание!'

    def get_addr_by_unique_code(self, code):
        return self.houses[code]

    def get_all_addr(self):
        return self.houses

# Начинаем строить город:


# Инициализируем Здания:
house_1 = Building(1, HOUSE_TYPE_ENUM['1'])
house_2 = Building(2, HOUSE_TYPE_ENUM['2'])
house_3 = Building(3, HOUSE_TYPE_ENUM['3'])
house_4 = Building(4, HOUSE_TYPE_ENUM['4'])
house_5 = Building(4, HOUSE_TYPE_ENUM['4'])
house_6 = Building(4, HOUSE_TYPE_ENUM['4'])
house_7 = Building(4, HOUSE_TYPE_ENUM['4'])

# Инициализируем Город Хабаровск
KHABAROVSK = City("Хабаровск")

# Выдаём всем зданиям цвета, т.к. без цвета дом не построится:
house_1.set_color('red')
house_2.set_color('red')
house_3.set_color('red')
house_4.set_color('white')
house_5.set_color('black')
house_6.set_color('yellow')
house_7.set_color('green')

# Выдаём всем домам кол-во этажей, т.к. без них они не построятся
house_1.set_quantity_floor(1)
house_2.set_quantity_floor(10)
house_3.set_quantity_floor(10)
house_4.set_quantity_floor(10)
house_5.set_quantity_floor(15)
house_6.set_quantity_floor(15)
house_7.set_quantity_floor(20)

Building.build_all()

KHABAROVSK.add_addr(house_1)
KHABAROVSK.add_addr(house_2)
KHABAROVSK.add_addr(house_3)
KHABAROVSK.add_addr(house_4)
KHABAROVSK.add_addr(house_5)
KHABAROVSK.add_addr(house_6)
KHABAROVSK.add_addr(house_7)

[print(value) for key, value in KHABAROVSK.get_all_addr().items()]


