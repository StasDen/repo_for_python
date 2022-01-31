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
    age_in_mounths_of_fish = 17.5
    weight_of_fish_in_kg = 3.2
    fish_names_list = ["Salmon", "Tuna", "Carp", "Cod", "Swordship"] # Example of a list(list is ordered, changeable)

    def sell_fish(self, name_of_fish):  # Relevant function if only I was a fish shop
        self.name_of_fish = name_of_fish

    def print_sold_fish(self, sold_fish: str) -> None:
        self.sold_fish = sold_fish
        self.sentence_about_sold_fish = "2 kg of " + sold_fish + " have been sold."
        print(self.sentence_about_sold_fish)

    def buy_fish(self, name_of_fish):  # Same function as above
        self.name_of_fish = name_of_fish

    def print_bought_fish(self, bought_fish: str) -> None:
        self.bought_fish = bought_fish
        self.sentence_about_bought_fish = "3 boxes of " + bought_fish + " have been bought."
        print(self.sentence_about_bought_fish)

    def __init__(self, name_of_fish) -> None:
        self.name_of_fish = name_of_fish

        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime.date(2022, 1, 21) # !datetime.SOMETHING(date, time, datetime) is working
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100


class FishInfo:
    name_of_fish = "Bream"
    price_in_uah_per_kilo = 70
    is_fresh_due_date = datetime.date(2022, 2, 2) # datetime.date(year, month, date)
    origin_of_fish = "Ukraine"
    catch_date_of_fish = datetime.datetime(2022, 1, 30, 17, 35) # datetime.datetime(year, month, date, hour, minute...)

    def __init__(self, name_of_fish: str = "", price_in_uah_per_kilo: str = "") -> None: # def__init__ - oleh = Student("oleh", "petrovych")
        self.name_of_fish = name_of_fish
        self.price_in_uah_per_kg = price_in_uah_per_kilo


class FishBox:
    roach = FishInfo("Roach", "86")

    weight_of_fish_in_kilo = 12.4
    package_date_of_fish = datetime.datetime(2022, 1, 29, 14, 29)

    height_of_fish_box_in_m = 1.5
    length_of_fish_box = 2.1
    width_of_fish_box = 0.8
    is_fish_alive_in_fish_box = bool(roach) # Example of using 'bool': bool_is_cool = 0 / print(bool(bool_is_cool)). Output: True


class FishShop:
    fish_boxes_dict = {
        "2033": "Salmon",  # It's dictionary
        "4012": "Carp",
        "1988": "Swordfish"  # Structure: code_of_box(identity) : fish_name
    }

    # fresh_fish_dict = {
    #     "Salmon": 120,
    #     "Carp": 90,
    #     "Cod": 105
    # }

    name_of_fish_shop = "Svizhak"
    sentence_of_announcement_of_fish_shop = "The fish shop " + "'" + name_of_fish_shop + "'" + " is inviting you!"
    address_of_fish_shop = "Kopernyka street, 39"
    when_fish_shop_is_open = "9:00 - 18:00"
    day_off_of_fish_shop = "Sunday"
    _fish_which_can_be_bought = "Salmon, tuna, carp, cod, swordfish"  # Protected
    __income_of_fish_shop_per_year_in_uah = 100000  # Private

    print(sentence_of_announcement_of_fish_shop)

    def __init__(self, name_of_fish) -> None:
        self.name_of_fish = name_of_fish

    def add_fish(self, fish_name: str, total_weight: float) -> None:  # For class 'Fish'
        self.fish_name = fish_name
        self.total_weight = total_weight

    def add_fish(self, fish_name: str, total_weight: float) -> None:  # For class 'FishBox'
        self.fish_name = fish_name
        self.total_weight = total_weight

    def get_fish_names_sorted_by_price(self, fresh_fish_dict, sorted_fresh_fish_dict) -> List[Union[str, float]]: # ?Possible realization of sorting
        self.fresh_fish_dict = fresh_fish_dict

        fresh_fish_dict = {
            "Salmon": 120,
            "Carp": 90,
            "Cod": 105
        }

        self.sorted_fresh_fish_dict = sorted_fresh_fish_dict
        sorted_fresh_fish_dict = sorted(fresh_fish_dict.items(), key = lambda x: x[1], reverse = True) # In descending order of values(example)
        print(sorted_fresh_fish_dict)

    def sell_fish(self, fish_name: str, weight_of_fish: float, is_fish_fresh: bool) -> Union[str, float, float]:
        self.fish_name = fish_name
        self.weight_of_fish = weight_of_fish
        self.is_fish_fresh = is_fish_fresh

    def get_frozen_fish_names_sorted_by_price(self, frozen_fish_names_sorted_by_price) -> list[str, bool, float]: # ?Tuple
        self.frozen_fish_names_sorted_by_price = frozen_fish_names_sorted_by_price
        print(self.frozen_fish_names_sorted_by_price)
        pass  # I'm sorting too...

    def get_fresh_fish_names_sorted_by_price(self, fresh_fish_names_sorted_by_price) -> list[str, bool, float]:
        self.fresh_fish_names_sorted_by_price = fresh_fish_names_sorted_by_price
        print(self.fresh_fish_names_sorted_by_price)
        pass  # Sorting is hard...

    def cast_out_old_fish(self) -> list[Union[str, float]]:
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

sold_salmon = Fish("Salmon")
sold_salmon.print_sold_fish("salmon")

bought_tuna = Fish("Tuna")
bought_tuna.print_bought_fish("tuna")

roach = FishShop("Roach")  # Example of method
roach.add_fish("Roach", 0.4)  # (name, weight)
