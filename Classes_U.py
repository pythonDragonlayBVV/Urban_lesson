class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mose=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mose

    def __repr__(self):
        return f'Видео "{self.title}"'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def nicknames(self):
        names = []
        for i in self.users:
            names.append(i.nickname)
        return names

    def log_in(self):
        self.log_out()
        switch = True
        if self.current_user is not None:
            print('Для того, чтобы войти в новый аккаунт, необходимо выйти из старого.')
            return
        names = self.nicknames()
        while switch:
            nickname = input('Пожалуйста, введите логин: ')
            if nickname not in names:
                print(f'Пользователь {nickname} не найден. Попробуйте ещё раз')
            else:
                password = input('Пожалуйста, введите пароль: ')
                for i in self.users:
                    if i.nickname == nickname:
                        true_user = i
                        true_password = i.password
                if hash(password) != true_password:
                    print('Пароль не подходит. Попробуйте ещё раз.')
                else:
                    print(f'Авторизация пользователя {nickname} выполнена успешно.\n')
                    switch = False
                    self.current_user = true_user
                    return self.current_user

    def register(self):
        self.log_out()
        if self.current_user is not None:
            print('Для того, чтобы начать регистрацию, необходимо выйти из аккаунта')
            return
        print('РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ')
        switch = True
        while switch:
            nickname = str(input('Введите логин: '))
            if nickname in self.nicknames():
                print('Пользователь с таким именем уже существует.\n Выберете следующее действие:')
                print('0 - Выйти из режима регистрации\n1 - Попробовать ещё раз')
                switch = bool(int(input()))
            else:
                password = hash(input('Введите пароль: '))
                while switch:
                    age = int(input('Введите возраст пользователя:'))
                    if age >= 0 and age <= 150:
                        switch = False
                    else:
                        print('Пожалуйста, введите корректный возраст:')
                user = User(nickname, password, age)
                self.users.append(user)
                self.current_user = user
                print(f'Регистрация пользователя {nickname} завершена успешно.\n')

        return self.current_user

    def log_out(self):
        switch = True
        if self.current_user is not None:
            print('Вы точно хотите выйти?\n  0 - Нет\n  1 - Да')
            switch = bool(int(input()))
            if switch:
                print(f'{self.current_user.nickname} вышел.')
                self.current_user = None
            else:
                return
        return self.current_user

    def add(self, *videos: Video):
        titles = set()
        for i in videos:
            for j in self.videos:
                titles.add(j.title)
            if i.title not in titles:
                self.videos.append(i)

    def get_videos(self, Search: str):
        titles = []
        Search = Search.lower()
        for j in self.videos:
            if Search in str(j.title).lower():
                titles.append(j.title)
        return titles

    def watch_video(self, watch_title):
        from time import sleep
        if self.current_user is None:
            print('Чтобы смотреть видео, войдите в аккаунт или зарегистрируйтесь')
            switch = bool(int(input('0 - Зарегистрироваться\n1 - Войти\n')))
            if switch:
                self.log_in()
            else:
                self.register()
        if self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        for i in self.videos:
            if i.title == watch_title:
                print('Просмотр видео начался')
                for j in range(1, i.duration+1):
                    print(j)
                    sleep(1)
                print('Просмотр видео окончен')
                i.time_now = i.duration