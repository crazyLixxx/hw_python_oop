class InfoMessage:
    """Информационное сообщение о тренировке."""
    print(Training.show_training_info())


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action,
        self.duration = duration,
        self.weight = weight

<<<<<<< HEAD
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def get_distance(self, action) -> float:
=======
    LEN_STEP = len_step(type_of_training)
        if types_of_trainings == Swimming:
            return action * 1.38
        else:
            return action * 0.65

    M_IN_KM = 1000

    def get_distance(self, ) -> float:
>>>>>>> ae6bcd79c39a458b2ca053208cf76a19f654cb92
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = length_pool
        self.count_pool = count_pool
    
<<<<<<< HEAD
    LEN_STEP = 1.36   

=======
>>>>>>> ae6bcd79c39a458b2ca053208cf76a19f654cb92
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return length_pool * count_pool / M_IN_KM / duration
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (self.get_mean_speed + 1.1) * 2 *  weight


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    types_of_trainings{
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    if workout_type == 'SWM'
        return type_of_trainings[workout_type](action = data[1], )
    
    
    
    return type_of_trainings[workout_type](data)


def main(training: Training) -> None:
    """Главная функция."""
    show_training_info(Training)

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

