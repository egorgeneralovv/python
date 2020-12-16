class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"зарплата": wage, "бонус": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + '' + self.surname

    def get_total_income(self):
        return self._income.get("зарплата") + self._income.get("бонус")
        # return f'{sum (self._доход.ценности())}'


a = Position("Александр", " Беглов ", "Мэр", 200000, 75000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
