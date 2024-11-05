import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.__enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.__enemies > 0:
            self.__enemies -= self.power
            day += 1
            if self.__enemies <= 0:
                self.__enemies = 0
            print(f'{self.name} сражается {day} день(дня), осталось {self.__enemies} воинов.')
            time.sleep(1)
        if self.__enemies <= 0:
            print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 243)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()