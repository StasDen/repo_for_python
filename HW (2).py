import datetime
from typing import List, Union
from unicodedata import name
# method
# attributes


class Student:
    group = "IP-11"

    def __init__(self, first_name: str = "", last_name: str = "") -> None:
        self.first_name = first_name    # public
        self.last_name = last_name      
        self.__name = "hidden"          # private
        self._another = "another"       # protected

    def print_name(self):
        self.full_name = "Mr/Mrs. " + self.first_name + " " + self.last_name
        print(self.full_name)

    @staticmethod
    def pass_exam() -> None:
        print(Student.group)


class Dean:
    pass


class Fish: 
    def sell_fish(self, name_of_fish): # Relevant function if only I was a fish shop
        self.name_of_fish = name_of_fish

    def print_sold_fish(self, sold_fish: str) -> None:
        self.sold_fish = sold_fish
        self.sentence_about_sold_fish = "2 kg of " + sold_fish + " have been sold."
        print(self.sentence_about_sold_fish)

    def buy_fish(self, name_of_fish): # Same function as above
        self.name_of_fish = name_of_fish

    def print_bought_fish(self, bought_fish: str) -> None:
        self.bought_fish = bought_fish
        self.sentence_about_bought_fish = "3 boxes of " + bought_fish + " have been bought."
        print(self.sentence_about_bought_fish)

    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        # self.catch_date = datetime("21/01/2022") ?Isn't working
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100


class FishShop:
    name_of_fish_shop = "Svizhak"
    sentence_of_announcement_of_fish_shop = "The fish shop " + "'" + name_of_fish_shop + "'" + " is inviting you!"
    address_of_fish_shop = "Kopernyka street, 39"
    when_fish_shop_is_open = "9:00 - 18:00"
    day_off_of_fish_shop = "Sunday"
    _fish_which_can_be_bought = "Salmon, tuna, carp, cod, swordfish"  # Protected
    __income_of_fish_shop_per_year_in_uah = 100000  # Private

    print(sentence_of_announcement_of_fish_shop)

    def add_fish(self, fish_name: str, total_weight: float) -> None:
        pass

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass

    def sell_fish1(self, fish_name: str, weight: float) -> float:
        pass

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        pass


class Seller:
    pass


class Buyer:
    pass


# oleh = Student("oleh", "petrovych")
# oleh.print_name()
# taras = Student()
# taras.print_name()
# vasyl = Dean()

sold_salmon = Fish()
sold_salmon.print_sold_fish("salmon")

bought_tuna = Fish()
bought_tuna.print_bought_fish("tuna")