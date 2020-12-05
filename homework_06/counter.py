"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter = 0

    def __new__(Cls):
        cls.counter += 1
        instance = super(cls, Cls).__new__(Cls)
        return instance

    cls.__new__ = __new__

    def get_created_instances(*self):
        return cls.counter

    def reset_instances_counter(*self):
        cls.counter, count_last = 0, cls.counter
        return count_last

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass
