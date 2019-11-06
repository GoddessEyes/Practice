from abc import ABC
from time import sleep
from random import randint
from collections import defaultdict
import weakref


class Animal:
    def __init__(self, name):
        self.name = name

    def say_your_phrase(self):
        raise NotImplementedError

    def moving(self, step):
        raise NotImplementedError

    def say_your_name(self):
        print(f'Меня зовут {self.name}')


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.step = 10
        self.phrase = 'Meow! Meow! Meow!'

    def say_your_phrase(self):
        return self.phrase

    def moving(self, step):
        return f'Кошечка {self.name} прошла {step} шагов!'

    def __set_name__(self, owner, name):
        self.name = name


asuka_cat = Cat('Асочка')


class Dog(Animal, ABC):
    __refs__ = defaultdict(list)

    def __init__(self, name, step, burk, rawr):
        super(Dog, self).__init__(name)
        self.rawr = rawr
        self.burk = burk
        self.step = step
        self.sleep_time = 0
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        isinstance_list = []
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                isinstance_list.append(inst)
        return isinstance_list

    def do_rawr(self, quantity_raw):
        for i in range(quantity_raw):
            print(f'{self.name} рычит: {self.rawr}')
            self.sleep_time += 1
            sleep(0.4)
        self.do_sleep()

    def do_bark(self, quantity_burk):
        for i in range(quantity_burk):
            print(f'{self.name} гавкает: {self.burk}')
            self.sleep_time += 1
            sleep(0.4)
        self.do_sleep()

    def moving(self, step):
        for i in range(step):
            print(
                f'{self.name} сделала {i} шагов! Через {step - i} '
                f'шагов пёсик устанет'
            )
            self.sleep_time += 1
            sleep(0.4)
        print(f'{self.name} устала')
        self.do_sleep()

    def do_sleep(self):
        sleep(self.sleep_time)
        self.sleep_time = 0


class DogsLife:
    def __init__(self, dog_list, time):
        self.dog_list = dog_list
        self.time = time

    def run_live(self):
        while self.time != 0:
            for dog in self.dog_list:
                if dog.sleep_time == 0:
                    rand_method = randint(1, 4)
                    if rand_method == 1:
                        dog.do_bark(quantity_burk=randint(0, 4))
                        continue
                    elif rand_method == 2:
                        dog.do_rawr(quantity_raw=randint(0, 4))
                        continue
                    elif rand_method == 3:
                        dog.moving(step=randint(0, 4))
                        continue
                    elif rand_method == 4:
                        dog.say_your_name()
                        dog.do_sleep()
                else:
                    continue
            self.time -= 1


plushka = Dog(name='Плюшка', step=2, burk='Вуф вуф!!!', rawr='РРРРРРРРь')


try:
    DogsLife(Dog.get_instances(), 10).run_live()
except KeyboardInterrupt:
    [dog.do_sleep() for dog in Dog.get_instances()]
    print('ВЫ закончили программу! Все собачки легли спать')
    SystemExit()



