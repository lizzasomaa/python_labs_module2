class Tree:
    """
    Базовый класс для хвойных деревьев.
    Атрибуты:
        name (str): Название дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Конструктор класса Tree.
        name: название дерева.
        height: высота дерева в метрах.
        age: возраст дерева в годах.
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        :return: Строка с информацией о дереве.
        """
        return f"{self.name}, высота: {self.height} м, возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        :return: Формальная строка с информацией о дереве.
        """
        return f"Tree(name={self.name}, height={self.height}, age={self.age})"

    def grow(self, years: int) -> None:
        """
        Увеличения возраста дерева и его высоты.
        years: Количество лет, на которое дерево растет.
        """
        self.age += years
        self.height += years * 0.5  # Предположим, что дерево растет на 0.5 метра в год.

    def get_description(self) -> str:
        """
        Возвращает вид дерева.
        return: Строка с описанием.
        """
        return f"Это дерево вида {self.name}."

class Pine(Tree):
    """
    Дочерний класс для сосны.
    Атрибуты:
        name (str): Название дерева (по умолчанию "Сосна").
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
        cone_count (int): Количество шишек на дереве.
    """

    def __init__(self, height: float, age: int, cone_count: int = 0):
        """
        Конструктор класса Pine.
        height: Высота дерева в метрах.
        age: Возраст дерева в годах.
        cone_count: Количество шишек на дереве (по умолчанию 0).
        """
        super().__init__(name="Сосна", height=height, age=age)
        self.cone_count = cone_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        return: Строка с информацией о сосне.
        """
        return f"{self.name}, высота: {self.height} м, возраст: {self.age} лет, шишек: {self.cone_count}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        return: Формальная строка с информацией о сосне.
        """
        return f"Pine(name={self.name}, height={self.height}, age={self.age}, cone_count={self.cone_count})"

    def get_description(self) -> str:
        """
        Перегруженный метод для получения описания сосны.
        return: Строка с описанием.
        """
        return f"Это сосна. Количество шишек: {self.cone_count}."

    def produce_cones(self, count: int) -> str:
        """
        Метод, описывающий, как сосна производит шишки.
        count: Количество шишек, которые производит дерево.
        return: Строка с описанием действия.
        """
        self.cone_count += count
        return f"{self.name} производит {count} шишек."

class Spruce(Tree):
    """
    Дочерний класс для ели.
    Атрибуты:
        name (str): Название дерева (по умолчанию "Ель").
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
        needle_color (str): Цвет хвои.
    """

    def __init__(self, height: float, age: int, needle_color: str = "зеленый"):
        """
        Конструктор класса Spruce.
        height: Высота дерева в метрах.
        age: Возраст дерева в годах.
        needle_color: Цвет хвои (по умолчанию "зеленый").
        """
        super().__init__(name="Ель", height=height, age=age)
        self.needle_color = needle_color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        return: Строка с информацией о ели.
        """
        return f"{self.name}, высота: {self.height} м, возраст: {self.age} лет, цвет хвои: {self.needle_color}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        return: Формальная строка с информацией о ели.
        """
        return f"Spruce(name={self.name}, height={self.height}, age={self.age}, needle_color={self.needle_color})"

    def get_description(self) -> str:
        """
        Перегруженный метод для получения описания ели.
        return: Строка с описанием.
        """
        return f"Это ель. Цвет хвои: {self.needle_color}."

    def drop_needles(self) -> str:
        """
        Метод, описывающий, как ель сбрасывает хвою.
        return: Строка с описанием действия.
        """
        return f"{self.name} сбрасывает хвою осенью."

if __name__ == "__main__":

    spruce = Spruce(height=10.5, age=25, needle_color="темно-зеленый")
    pine = Pine(height=15.0, age=30, cone_count=20)

    print(spruce)  # Ель, высота: 10.5 м, возраст: 25 лет, цвет хвои: темно-зеленый
    print(pine)  # Сосна, высота: 15.0 м, возраст: 30 лет, шишек: 20

    print(spruce.get_description())  # Это ель. Цвет хвои: темно-зеленый.
    print(pine.get_description())  # Это сосна. Количество шишек: 20.

    print(spruce.drop_needles())  # Ель сбрасывает хвою осенью.
    print(pine.produce_cones(5))  # Сосна производит 5 шишек.
    pass
