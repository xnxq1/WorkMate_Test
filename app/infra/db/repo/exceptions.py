from dataclasses import dataclass


class BaseRepoException(Exception):

    @property
    def message(self):
        return f'Ошибка репозитория'

@dataclass
class NotCatException(Exception):
    cat_id: int

    @property
    def message(self):
        return f'Кота с id {self.cat_id} нет'



@dataclass
class NotCatsWithThisBreedException(Exception):
    breed_name: str

    @property
    def message(self):
        return f'Котов с породой {self.breed_name} нет'