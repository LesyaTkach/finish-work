from typing import List


# Базовый класс для социальной сети
class SocialNetwork:
    """
    Базовый класс для социальной сети. Включает общие атрибуты и методы для всех социальных сетей.
    """

    def __init__(self, name: str, users_count: int, launch_year: int):
        """
        Инициализация базового класса социальной сети.

        :param name: Название социальной сети
        :param users_count: Количество пользователей
        :param launch_year: Год запуска социальной сети
        """
        self.name = name
        self.users_count = users_count
        self.launch_year = launch_year

    def __str__(self) -> str:
        """
        Строковое представление объекта социальной сети.

        :return: строка с названием и годом запуска
        """
        return f"{self.name} запущена в {self.launch_year} году."

    def __repr__(self) -> str:
        """
        Описание объекта в виде строки.

        :return: строка с подробным описанием социальной сети
        """
        return f"SocialNetwork(name='{self.name}', users_count={self.users_count}, launch_year={self.launch_year})"

    def get_user_count(self) -> int:
        """
        Возвращает количество пользователей социальной сети.

        :return: количество пользователей
        """
        return self.users_count


# Дочерний класс для VK
class VK(SocialNetwork):
    """
    Класс для социальной сети VK, наследующий от SocialNetwork.
    Включает дополнительные атрибуты и методы.
    """

    def __init__(self, users_count: int, launch_year: int, vk_version: str):
        """
        Инициализация для VK с добавлением версии.

        :param users_count: Количество пользователей
        :param launch_year: Год запуска
        :param vk_version: Версия социальной сети
        """
        # Используем конструктор базового класса
        super().__init__('VK', users_count, launch_year)
        self.vk_version = vk_version

    def __str__(self) -> str:
        """
        Перегруженный метод __str__, чтобы включить версию VK.

        :return: строка с названием, годом запуска и версией VK
        """
        return f"VK (версия {self.vk_version}) запущена в {self.launch_year} году."

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__, добавлен атрибут версии.

        :return: строка с подробным описанием VK
        """
        return f"VK(users_count={self.users_count}, launch_year={self.launch_year}, vk_version='{self.vk_version}')"

    def get_user_count(self) -> int:
        """
        Переопределенный метод получения количества пользователей.

        Причина: метод может учитывать активных пользователей, если необходимо.

        :return: количество пользователей
        """
        return self.users_count


# Дочерний класс для Facebook
class Facebook(SocialNetwork):
    """
    Класс для социальной сети Facebook, наследующий от SocialNetwork.
    Включает дополнительные атрибуты и методы.
    """

    def __init__(self, users_count: int, launch_year: int, is_meta: bool):
        """
        Инициализация для Facebook с добавлением информации о Meta.

        :param users_count: Количество пользователей
        :param launch_year: Год запуска
        :param is_meta: Признак принадлежности к Meta
        """
        # Используем конструктор базового класса
        super().__init__('Facebook', users_count, launch_year)
        self.is_meta = is_meta

    def __str__(self) -> str:
        """
        Перегруженный метод __str__, чтобы включить информацию о Meta.

        :return: строка с названием, годом запуска и информацией о Meta
        """
        meta_status = "является частью Meta" if self.is_meta else "не является частью Meta"
        return f"Facebook (запущен в {self.launch_year} году) {meta_status}."

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__, добавлен атрибут is_meta.

        :return: строка с подробным описанием Facebook
        """
        return f"Facebook(users_count={self.users_count}, launch_year={self.launch_year}, is_meta={self.is_meta})"

    def get_user_count(self) -> int:
        """
        Переопределенный метод получения количества пользователей, с возможностью учитывать изменения из-за политики Meta.

        :return: количество пользователей
        """
        # Пример логики: если социальная сеть является частью Meta, то количество пользователей может быть другим
        if self.is_meta:
            return self.users_count * 1.1  # Прибавим 10% если это Meta
        return self.users_count


# Основной код
if __name__ == "__main__":
    # Создаем экземпляры классов
    vk = VK(users_count=100000000, launch_year=2006, vk_version="5.1")
    facebook = Facebook(users_count=2900000000, launch_year=2004, is_meta=True)

    # Выводим информацию о социальных сетях
    print(vk)  # Перегруженный метод __str__
    print(repr(vk))  # Перегруженный метод __repr__

    print(facebook)  # Перегруженный метод __str__
    print(repr(facebook))  # Перегруженный метод __repr__

    # Пример использования метода get_user_count
    print(f"Количество пользователей VK: {vk.get_user_count()}")
    print(f"Количество пользователей Facebook: {facebook.get_user_count()}")

