

class BaseAppException(Exception):

    @property
    def message(self):
        return f'Ошибка приложения'