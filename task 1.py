# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, material: str, height: float, width: float) -> None:
        """
        Инициализация стола.

        :param material: Материал стола (например, дерево, металл).
        :param height: Высота стола в сантиметрах (должна быть положительной).
        :param width: Ширина стола в сантиметрах (должна быть положительной).

        :raises ValueError: Если height или width не положительные.

        >>> table = Table("дерево", 75.0, 120.0)
        >>> table.material
        'дерево'
        """
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина должны быть положительными числами.")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def resize(self, new_height: float, new_width: float) -> None:
        """
        Изменяет размеры стола.

        :param new_height: Новая высота стола.
        :param new_width: Новая ширина стола.

        >>> table.resize(80.0, 140.0)
        """
        ...

    @abstractmethod
    def clean(self) -> None:
        """
        Очищает поверхность стола.

        >>> table.clean()
        """
        ...


class Tree(ABC):
    def __init__(self, species: str, age: int) -> None:
        """
        Инициализация дерева.

        :param species: Вид дерева (например, дуб, сосна).
        :param age: Возраст дерева в годах (должен быть неотрицательным).

        :raises ValueError: Если age отрицательное.

        >>> tree = Tree("дуб", 50)
        >>> tree.species
        'дуб'
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева.

        :param years: Количество лет для увеличения возраста.

        >>> tree.grow(5)
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбрасывает листья дерева.

        >>> tree.shed_leaves()
        """
        ...


class SocialNetwork(ABC):
    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация социальной сети.

        :param name: Название социальной сети (например, Facebook).
        :param user_count: Количество пользователей (должно быть неотрицательным).

        :raises ValueError: Если user_count отрицательное.

        >>> network = SocialNetwork("Facebook", 2000000000)
        >>> network.name
        'Facebook'
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.user_count = user_count

    @abstractmethod
    def add_user(self) -> None:
        """
        Добавляет нового пользователя в сеть.

        >>> network.add_user()
        """
        ...

    @abstractmethod
    def remove_user(self) -> None:
        """
        Удаляет пользователя из сети.

        >>> network.remove_user()
        """

    ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
