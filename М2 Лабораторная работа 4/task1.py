if __name__ == "__main__":
    # Write your solution here
    pass


from typing import List


# = ТРАНСПОРТ =

class Transport:
    """Базовый класс для всех видов транспорта.

    Атрибуты:
        _name (str): Название транспортного средства
        _capacity (int): Вместимость
        _speed (float): Максимальная скорость (км/ч)
        _year (int): Год выпуска
    """

    def __init__(self, name: str, capacity: int, speed: float, year: int) -> None:
        self._name = name
        self._capacity = capacity
        self._speed = speed
        self._year = year
        self._is_moving = False

    @property
    def name(self) -> str: return self._name

    @property
    def capacity(self) -> int: return self._capacity

    @property
    def speed(self) -> float: return self._speed

    @property
    def year(self) -> int: return self._year

    def start(self) -> None:
        self._is_moving = True
        print(f"{self._name} начал движение")

    def stop(self) -> None:
        self._is_moving = False
        print(f"{self._name} остановился")

    def get_info(self) -> str:
        return f"{self._name} ({self._year} г.), вместимость: {self._capacity}, скорость: {self._speed} км/ч"

    def __str__(self) -> str:
        return f"Транспорт: {self._name}, {self._year} г."

    def __repr__(self) -> str:
        return f"Transport(name='{self._name}', capacity={self._capacity}, speed={self._speed}, year={self._year})"


class LandTransport(Transport):
    """Наземный транспорт.

    Добавляет атрибуты:
        _wheel_count (int): Количество колес
        _fuel_type (str): Тип топлива
        _terrain_type (str): Тип местности
    """

    def __init__(self, name: str, capacity: int, speed: float, year: int,
                 wheel_count: int, fuel_type: str, terrain_type: str = "шоссе") -> None:
        super().__init__(name, capacity, speed, year)
        self._wheel_count = wheel_count
        self._fuel_type = fuel_type
        self._terrain_type = terrain_type

    @property
    def wheel_count(self) -> int: return self._wheel_count

    @property
    def fuel_type(self) -> str: return self._fuel_type

    @property
    def terrain_type(self) -> str: return self._terrain_type

    @terrain_type.setter
    def terrain_type(self, value: str) -> None:
        valid = ["шоссе", "бездорожье", "город", "трасса"]
        if value not in valid:
            raise ValueError(f"Допустимо: {valid}")
        self._terrain_type = value

    def start(self) -> None:
        """Перегружен: добавлена проверка дороги."""
        print(f"{self._name} выезжает на {self._terrain_type}")
        super().start()

    def get_max_range(self) -> float:
        """Новый метод: расчет пробега."""
        return 500 * 100 / (self._wheel_count * 2)

    def __str__(self) -> str:
        return f"Наземный транспорт: {self._name}, {self._fuel_type}, колес: {self._wheel_count}"

    def __repr__(self) -> str:
        return (f"LandTransport(name='{self._name}', capacity={self._capacity}, "
                f"speed={self._speed}, year={self._year}, wheel_count={self._wheel_count}, "
                f"fuel_type='{self._fuel_type}', terrain_type='{self._terrain_type}')")


class WaterTransport(Transport):
    """Водный транспорт.

    Добавляет атрибуты:
        _displacement (float): Водоизмещение (т)
        _propulsion_type (str): Тип движителя
        _max_draft (float): Осадка (м)
    """

    def __init__(self, name: str, capacity: int, speed: float, year: int,
                 displacement: float, propulsion_type: str, max_draft: float) -> None:
        super().__init__(name, capacity, speed, year)
        self._displacement = displacement
        self._propulsion_type = propulsion_type
        self._max_draft = max_draft

    @property
    def displacement(self) -> float:
        return self._displacement

    @property
    def propulsion_type(self) -> str:
        return self._propulsion_type

    @property
    def max_draft(self) -> float:
        return self._max_draft

    def start(self) -> None:
        """Перегружен: проверка глубины."""
        print(f"Проверка глубины: требуется ≥ {self._max_draft} м")
        print(f"{self._name} отчаливает")
        super().start()

    def get_sea_state_limit(self, wave_height: float) -> str:
        """Новый метод: ограничение по волнам."""
        if wave_height <= 1.0:
            return "можно выходить в море"
        if wave_height <= 3.0:
            return "ограниченное плавание"
        return "оставаться в порту"

    def __str__(self) -> str:
        return f"Водный транспорт: {self._name}, водоизмещение: {self._displacement} т"

    def __repr__(self) -> str:
        return (f"WaterTransport(name='{self._name}', capacity={self._capacity}, "
                f"speed={self._speed}, year={self._year}, displacement={self._displacement}, "
                f"propulsion_type='{self._propulsion_type}', max_draft={self._max_draft})")


# = СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ =

class BuildingMaterial:
    """Базовый класс строительных материалов."""

    def __init__(self, name: str, density: float, strength: float, price: float) -> None:
        self._name = name
        self._density = density
        self._strength = strength
        self._price = price

    @property
    def name(self) -> str: return self._name

    @property
    def density(self) -> float: return self._density

    @property
    def strength(self) -> float: return self._strength

    @property
    def price(self) -> float: return self._price

    def calculate_weight(self, volume: float) -> float:
        return volume * self._density

    def get_info(self) -> str:
        return f"{self._name}: плотность {self._density} кг/м³, прочность {self._strength} МПа"

    def __str__(self) -> str:
        return f"Материал: {self._name}"

    def __repr__(self) -> str:
        return f"BuildingMaterial(name='{self._name}', density={self._density}, strength={self._strength}, price={self._price})"


class NaturalMaterial(BuildingMaterial):
    """Природные материалы."""

    def __init__(self, name: str, density: float, strength: float, price: float,
                 origin: str, is_renewable: bool, extraction_method: str) -> None:
        super().__init__(name, density, strength, price)
        self._origin = origin
        self._is_renewable = is_renewable
        self._extraction_method = extraction_method

    @property
    def origin(self) -> str: return self._origin

    @property
    def is_renewable(self) -> bool: return self._is_renewable

    @property
    def extraction_method(self) -> str: return self._extraction_method

    def calculate_weight(self, volume: float) -> float:
        """Перегружен: учет влажности."""
        base = super().calculate_weight(volume)
        factor = 1.1 if "древесина" in self._name.lower() else 1.05
        return base * factor

    def get_environmental_impact(self) -> str:
        """Новый метод: эко-оценка."""
        if self._is_renewable:
            return "низкое воздействие, возобновляемый ресурс"
        return f"высокое воздействие (добыча: {self._extraction_method})"

    def __str__(self) -> str:
        return f"Природный материал: {self._name} ({self._origin})"

    def __repr__(self) -> str:
        return (f"NaturalMaterial(name='{self._name}', density={self._density}, "
                f"strength={self._strength}, price={self._price}, origin='{self._origin}', "
                f"is_renewable={self._is_renewable}, extraction_method='{self._extraction_method}')")


class ArtificialMaterial(BuildingMaterial):
    """Искусственные материалы."""

    def __init__(self, name: str, density: float, strength: float, price: float,
                 manufacturer: str, composition: str, production_method: str) -> None:
        super().__init__(name, density, strength, price)
        self._manufacturer = manufacturer
        self._composition = composition
        self._production_method = production_method

    @property
    def manufacturer(self) -> str: return self._manufacturer

    @property
    def composition(self) -> str: return self._composition

    @property
    def production_method(self) -> str: return self._production_method

    def get_info(self) -> str:
        """Перегружен: добавлен производитель."""
        return f"{super().get_info()}, производитель: {self._manufacturer}"

    def get_production_certificate(self) -> str:
        """Новый метод: сертификат."""
        return f"Сертификат ГОСТ для {self._name} ({self._production_method})"

    def __str__(self) -> str:
        return f"Искусственный материал: {self._name} ({self._manufacturer})"

    def __repr__(self) -> str:
        return (f"ArtificialMaterial(name='{self._name}', density={self._density}, "
                f"strength={self._strength}, price={self._price}, manufacturer='{self._manufacturer}', "
                f"composition='{self._composition}', production_method='{self._production_method}')")


# = ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ =

class Software:
    """Базовый класс ПО."""

    def __init__(self, name: str, version: str, developer: str, license_type: str) -> None:
        self._name = name
        self._version = version
        self._developer = developer
        self._license_type = license_type

    @property
    def name(self) -> str: return self._name

    @property
    def version(self) -> str: return self._version

    @property
    def developer(self) -> str: return self._developer

    @property
    def license_type(self) -> str: return self._license_type

    def install(self) -> None:
        print(f"Установка {self._name} {self._version}...")

    def uninstall(self) -> None:
        print(f"Удаление {self._name}...")

    def get_system_requirements(self) -> str:
        return "Минимальные требования: 2 ГБ ОЗУ, 500 МБ диска"

    def __str__(self) -> str:
        return f"ПО: {self._name} ({self._version})"

    def __repr__(self) -> str:
        return f"Software(name='{self._name}', version='{self._version}', developer='{self._developer}', license_type='{self._license_type}')"


class OperatingSystem(Software):
    """Операционные системы."""

    def __init__(self, name: str, version: str, developer: str, license_type: str,
                 kernel_type: str, architecture: List[str], has_gui: bool = True) -> None:
        super().__init__(name, version, developer, license_type)
        self._kernel_type = kernel_type
        self._architecture = architecture.copy()
        self._has_gui = has_gui

    @property
    def kernel_type(self) -> str:
        return self._kernel_type

    @property
    def architecture(self) -> List[str]:
        return self._architecture.copy()

    @property
    def has_gui(self) -> bool:
        return self._has_gui

    def install(self) -> None:
        """Перегружен: сложный процесс установки ОС."""
        print(f"Запуск установки ОС {self._name} {self._version}")
        print(f"Архитектуры: {', '.join(self._architecture)}")
        print("Создание разделов... Установка загрузчика... Настройка ядра...")
        print("Установка завершена")

    def get_system_requirements(self) -> str:
        """Перегружен: уточненные требования."""
        if "Windows" in self._name:
            return "Требования: 4 ГБ ОЗУ, 64 ГБ диска, 2-ядерный CPU"
        if "Linux" in self._name:
            return "Требования: 1 ГБ ОЗУ, 10 ГБ диска, любой CPU"
        return super().get_system_requirements()

    def boot(self) -> str:
        """Новый метод: загрузка ОС."""
        return f"Загрузка {self._name} (ядро: {self._kernel_type})"

    def __str__(self) -> str:
        gui = "с GUI" if self._has_gui else "без GUI"
        return f"ОС: {self._name} {self._version} ({self._kernel_type}, {gui})"

    def __repr__(self) -> str:
        return (f"OperatingSystem(name='{self._name}', version='{self._version}', "
                f"developer='{self._developer}', license_type='{self._license_type}', "
                f"kernel_type='{self._kernel_type}', architecture={self._architecture}, "
                f"has_gui={self._has_gui})")


class OfficeSoftware(Software):
    """Офисное ПО."""

    def __init__(self, name: str, version: str, developer: str, license_type: str,
                 applications: List[str], file_formats: List[str], cloud_support: bool = False) -> None:
        super().__init__(name, version, developer, license_type)
        self._applications = applications.copy()
        self._file_formats = file_formats.copy()
        self._cloud_support = cloud_support

    @property
    def applications(self) -> List[str]:
        return self._applications.copy()

    @property
    def file_formats(self) -> List[str]:
        return self._file_formats.copy()

    @property
    def cloud_support(self) -> bool:
        return self._cloud_support

    def install(self) -> None:
        """Перегружен: установка пакета приложений."""
        print(f"Установка офисного пакета {self._name} {self._version}")
        for app in self._applications:
            print(f"- {app}")
        print("Установка завершена")

    def get_system_requirements(self) -> str:
        """Перегружен: учет облака."""
        req = super().get_system_requirements()
        if self._cloud_support:
            req += ", требуется интернет"
        return req

    def open_document(self, filename: str) -> str:
        """Новый метод: открытие документа."""
        ext = filename.split('.')[-1] if '.' in filename else ""
        if ext.upper() in [f.upper() for f in self._file_formats]:
            return f"Открытие {filename}"
        return f"Формат .{ext} не поддерживается"

    def __str__(self) -> str:
        cloud = "с облаком" if self._cloud_support else "без облака"
        return f"Офисное ПО: {self._name} ({len(self._applications)} приложений, {cloud})"

    def __repr__(self) -> str:
        return (f"OfficeSoftware(name='{self._name}', version='{self._version}', "
                f"developer='{self._developer}', license_type='{self._license_type}', "
                f"applications={self._applications}, file_formats={self._file_formats}, "
                f"cloud_support={self._cloud_support})")


if __name__ == "__main__":
    print("=" * 70)
    print("ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ КЛАССОВ")
    print("=" * 70)

    # Транспорт
    print("\n--- ТРАНСПОРТ ---")
    bus = LandTransport("ЛиАЗ-5292", 110, 80, 2023, 6, "дизель", "город")
    boat = WaterTransport("Метеор-120", 120, 65, 2021, 45.0, "водомет", 1.2)

    print(bus)
    print(repr(bus))
    bus.start()
    print(f"Запас хода: {bus.get_max_range(): .1f} км")
    print(f"Ограничение по волнам: {boat.get_sea_state_limit(2.5)}")

    # Стройматериалы
    print("\n--- СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ ---")
    wood = NaturalMaterial("Сосна", 520, 40, 12000, "Сибирь", True, "лесозаготовка")
    concrete = ArtificialMaterial("Бетон М300", 2400, 300, 4500, "ООО Бетон",
                                  "цемент+песок+щебень", "вибролитье")

    print(wood)
    print(f"Вес 2м³: {wood.calculate_weight(2)} кг")
    print(f"Эко-оценка: {wood.get_environmental_impact()}")
    print(concrete.get_info())

    # ПО
    print("\n--- ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ---")
    windows = OperatingSystem("Windows 11", "22H2", "Microsoft", "проприетарная",
                              "гибридное", ["x64", "ARM64"])
    office = OfficeSoftware("LibreOffice", "7.5", "The Document Foundation", "GPL",
                            ["Writer", "Calc", "Impress"], ["ODT", "ODS", "ODP"], True)

    print(windows)
    print(windows.get_system_requirements())
    print(windows.boot())
    office.install()

    print("\n" + "=" * 70)
