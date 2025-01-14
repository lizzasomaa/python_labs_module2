import doctest

class Table:
    """
    объект: стол
    параметры:
        heigth - высота стола
        length - длина стола
        width - ширина стола
    Пример:
        >>> table = Table(80, 90, 100)
    """

    def __init__(self, height: float, length: float, width: float):
        self.height = None
        self.length = None
        self.width = None

        if height < 0 or length < 0 or width < 0:
            raise ValueError

        if isinstance(height, (int, float)) == False:
            raise TypeError
        if isinstance(length, (int, float)) == False:
            raise TypeError
        if isinstance(width, (int, float)) == False:
            raise TypeError

        self.height = height
        self.length = length
        self.width = width

    def table_area(self) -> (int, float):
        """
        функция, возвращающая площадь стола типа int или float
        площадь = length * wigth
        пример:
        >>> table = Table(80, 90, 100)
        >>> table.table_area()
        """
        ...

    def table_fit(self, obj_length, obj_width) -> bool:
        """
        функция, проверяющая поместится ли объект на столе
        аргументы:
            obj_length - длина объекта, помещаемого на стол
            obj_width - ширина объекта, помещаемого на стол
        если аргумент не типа (int, float), вызывается raise TypeError
        возвращает True, если площадь объекта меньше площади стола, False, если больше
        пример:
        >>> table = Table(80, 90, 100)
        >>> table.table_fit(80, 80)
        """
        ...


class Kettle:
    """
    объект: чайник
    параметры:
        volume - объем
        voltage - напряжение, необходимое для работы чайника
        is_on - включен ли чайник
    пример:
        >>> kettle = Kettle(2.5, 220, False)
    """

    def __init__(self, volume: float, voltage: float, is_on: bool):
        if volume < 0 or voltage < 0:
            raise ValueError

        if is_on != True and is_on != False:
            raise TypeError

        if isinstance(voltage, (int, float)) == False:
            raise TypeError

        self.volume = volume
        self.power = voltage
        self.is_on = is_on

    def change_state(self, state: bool) -> None:
        """
        функция, меняющая состояние чайника
        аргумент: state - состояние, которое нужно установить (0 - выключить, 1 - включить)
        меняет значение переменной is_on на state
        пример:
            >>> kettle = Kettle(2.5, 220, False)
            >>> kettle.change_state(True)
        """
        ...

    def check_voltage(self, main_voltage: float) -> bool:
        """
        функция, проверяющая, достаточное ли напряжение в розетке для работы чайника
        аргумент: main_votage - напряжение в розетке
        если аргумент не типа (int, float), вызывается raise TypeError
        возвращает True если напряжение в розетке больше напряжения чайника, False если оно меньше
        пример:
            >>> kettle = Kettle(2.5, 220, False)
            >>> kettle.check_voltage(230)
        """
        ...


class Fridge:
    """
    объект: холодильник
    параметры:
        temperature - поддерживаемая температура
        food - количество единиц еды в холодильнике
    пример:
        >>> fridge = Fridge(-1, 7)
    """

    def __init__(self, temperature: float, food: int):
        if food < 0:
            raise ValueError

        if isinstance(temperature, (int, float)) == False:
            raise TypeError
        if isinstance(food, int) == False:
            raise TypeError

        self.temperature = temperature
        self.shelves = food

    def change_temperature(self, new_temperature) -> None:
        """
        функция, изменяющая температуру внутри холодильника
        аргумент: new_temperature - новая температура
        если аргумент не типа (int, float), вызывается raise TypeError
        пример:
        >>> fridge = Fridge(-1, 7)
        >>> fridge.change_temperature(+5)
        """
        ...

    def take_food(self, number_of_food) -> None:
        """
        функция, уменьшающая число продуктов в холодильнике после того, как их взяли оттуда
        аргумент: number_of_food - количество взятых из холодильника позиций
        если аргумент не типа int, вызывается raise TypeError
        пример:
        >>> fridge = Fridge(-1, 7)
        >>> fridge.take_food(2)
        """



if __name__ == "__main__":
    doctest.testmod()
