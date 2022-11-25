class Auto():
    def __init__(self, number, mark, model, n, color, m, year, price):
        self.number = number
        self.mark = mark
        self.model = model
        self.n = n
        self.color = color
        self.m = m
        self.year = year
        self.price = price

    def __str__(self):
        return f"<{self.number} {self.mark} {self.model} {self.m} {self.color} {self.n} {self.year} " \
               f"{self.price}р.>"

    def update_price(self, new_price):
        self.price = new_price

    def __eq__(self, another):
        if self.year == another.year and self.m == another.m:
            return True
        return False

    def __lt__(self, another):
        if self.year != another.year:
            return self.year < another.year
        elif self.m != another.m:
            return self.m < another.m
        return False

    def __le__(self, another):
        if self.__eq__(another):
            return True
        if self.__lt__(another):
            return True
        return False


class Dealership():
    def __init__(self, name, adres, FIO, phone):
        self.name = name
        self.adres = adres
        self.FIO = FIO
        self.phone = phone
        self.aftosolon = []

    def insert_auto(self, auto):
        self.aftosolon.append(auto)

    def sale_auto(self, number):
        for auto in self.aftosolon:
            if auto.number == number:
                self.aftosolon.remove(auto)
                break

    def __str__(self):
        return f"«Салон:<{self.name}> {self.adres} {self.FIO} {self.phone}»"

    def print_autos(self):
        print(*self.aftosolon, sep="\n")

    def __eq__(self, other):
        nov_s = len(list(filter(lambda x: x.mileage == 'новый', self.aftosolon)))
        nov_o = len(list(filter(lambda x: x.mileage == 'новый', other.salon)))
        return len(self.aftosolon) == len(other.sp) and nov_s == nov_o

    def __lt__(self, another):  # <
        nov_s = len(list(filter(lambda x: x.mileage == 'новый', self.aftosolon)))
        nov_o = len(list(filter(lambda x: x.mileage == 'новый', another.sp)))
        if len(self.aftosolon) != len(another.salon):
            return len(self.aftosolon) < len(another.salon)
        elif len(self.aftosolon) == len(another.salon):
            return nov_s < nov_o
        return False

    def __le__(self, another):
        if self.__eq__(another):
            return True
        if self.__lt__(another):
            return True
        return False


emp_1 = Employee(1, 'Гречка', 110, 100, 34, 'кг')
emp_2 = Employee(2, 'Рис', 90,  110, 23, 'кг')