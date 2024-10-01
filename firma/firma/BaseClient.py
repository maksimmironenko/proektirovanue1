import re
from functools import total_ordering


@total_ordering
class BaseClient:
    
    def __init__(
        self,
        id,
        email,
        firstname, 
        surname, 
        fathersname,
    ):
        self.set_id(id)
        self.set_email(email)
        self.set_firstname(firstname)
        self.set_surname(surname)
        self.set_fathersname(fathersname)

    def set_id(self, id):
        self._id = self.__validate_id(id)

    def set_email(self, email):
        self._email = self.__validate_email(email)

    def set_firstname(self, firstname):
        self._firstname = self.__validate_fio(firstname)
    
    def set_surname(self, surname):
        self._surname = self.__validate_fio(surname)

    def set_fathersname(self, fathersname):
        self._fathersname = self.__validate_fio(fathersname, True)

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email
    
    def get_firstname(self):
        return self._firstname
    
    def get_surname(self):
        return self._surname
    
    def get_fathersname(self):
        return self._fathersname

    @staticmethod
    def __validate_id(id):
        if not isinstance(id, int) or not id>0:
            raise ValueError('Неверный id.')
        return id
    
    @staticmethod
    def __validate_email(email):
        if not isinstance(email, str) or not re.fullmatch(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', email):
            raise ValueError('Неверный email.')
        return email
    
    @staticmethod
    def __validate_fio(fio_field, is_fathersname=False):
        if not isinstance(fio_field, str) and not is_fathersname:
            raise ValueError('Имя и Фамилия должны быть строковыми.')
        if not fio_field and not is_fathersname:
            raise ValueError('ФИО не должно быть пустым')
        if ((is_fathersname and fio_field is not None) or not is_fathersname) and re.search(r'\d', fio_field) is not None:
                raise ValueError('ФИО не должно содеражть цифр.')
        return fio_field

    def __eq__(self, other):
        if self.get_email() != other.get_email():
            return False
        return True

    def __lt__(self, other):
        return self.get_surname() < other.get_surname()

    def __hash__(self):
        return hash(self.email)
    
    def __str__(self):
        return f'{self.get_id()} {self.get_surname()} {self.get_firstname()}'

    def __repr__(self):
        return self.__str__()
