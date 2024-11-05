from sql_actions import Select, Insert

class Repositorio:

    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_many()