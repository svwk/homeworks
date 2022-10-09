"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_number = 100
    min_number = 1

    while True:
        if max_number == number | min_number == number:
            return count

        count += 1

        predict_number = int(np.mean([min_number, max_number]))

        if predict_number > number:
            max_number = predict_number
            continue

        elif predict_number < number:
            min_number = predict_number
            continue

        else:
            break  # конец игры, выход из цикла

    return count


def score_game(random_predict_func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
