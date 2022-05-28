# Importing
from abc import ABC, abstractmethod

import random


# Superclass
class DigitalElement(ABC):  # Abstract class for inheritance

    # Creating initializer
    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int = 5) -> None:
        self._name = name
        self._working_time_in_years = working_time_in_years
        self._purchase_cost_in_usd = purchase_cost_in_usd

        print("New digital element has been added")

    # Implementing string representation of DigitalElement object
    def __str__(self) -> str:
        return (f"Element '{self._name}' works {self._working_time_in_years} years and costs"
                f" {self._purchase_cost_in_usd}$")

    # Some abstract methods
    @abstractmethod
    def meter(self, is_connected: bool) -> int | str:
        pass

    @abstractmethod
    def print_metered_info(self, device_has_been_used: bool) -> None:
        pass


# Subclasses
class BinaryCounter(DigitalElement):

    # Adding some different variable from parent class(inheritance)
    def __init__(self, name: str, purchase_cost_in_usd: int, _working_time_in_years: int,
                 max_metered_byte_sequence: int):
        super().__init__(name, purchase_cost_in_usd, max_metered_byte_sequence)  # super() method is necessary here
        self._max_metered_byte_sequence = max_metered_byte_sequence

    def __str__(self) -> str:
        return (f"Binary counter '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Max metered byte sequence: {self._max_metered_byte_sequence}")

    # Adding realizations to abstract methods
    def meter(self, is_connected: bool) -> int | str:  # We can return either int type or str
        output = random.randint(1, 100)  # Choosing random number from 1 to 100

        # Checking if element is connected
        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Connect your binary counter")


class DecadeCounter(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 counted_num_of_digits: int = 10) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._counted_num_of_digits = counted_num_of_digits

    def __str__(self) -> str:
        return (f"Decade counter '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Counted number of digits: {self._counted_num_of_digits}")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 100)  # Some number

        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Connect your decade counter")


class ReverseCounter(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 is_reverse_possible: bool = True) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._is_reverse_possible = is_reverse_possible

    def __str__(self) -> str:
        return (f"Reverse counter '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Is it true it reverses sequences of bytes? "
                f"{self._is_reverse_possible}")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 100)  # Some number

        if is_connected:
            return output
        else:
            return "Connect your reverse counter before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Connect your reverse counter")

    # Reversing input
    @staticmethod
    def reverse_sequence_of_bytes():
        number = int(input("Enter a sequence of bytes: "))  # Getting a sequence
        revs_number = 0

        while number > 0:
            remainder = number % 10  # Taking the last number

            revs_number = revs_number * 10 + remainder  # Creating the output
            number = number // 10  # Removing the last num

        print("Reversed sequence: {}".format(revs_number))


class Multiplexer(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 number_of_output_lines: int) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._number_of_output_lines = number_of_output_lines

    def __str__(self) -> str:
        return (f"Multiplexer '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Number of output lines: {self._number_of_output_lines}")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 100)  # Some number

        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Connect your multiplexer")

    # Forming single line from several input ones
    def forward_lines_to_single_output(self) -> None:

        # Showing some example
        print("Example: 21(1) 23(2)...")

        # Getting multiple values
        input_sequences = input(f"Input all {self._number_of_output_lines} lines here, like in example above: ")
        sequences_list = input_sequences.split()  # Creating list with input variables

        result = "".join(sequences_list)  # Joining list using join() method
        print(f"Output line: {result}")


class DelayFlipFlop(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 max_delaying_time_in_sec: int = 5) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._max_delaying_time_in_sec = max_delaying_time_in_sec

    def __str__(self) -> str:
        return (f"D flip-flop '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. {self._max_delaying_time_in_sec} sec - is max delaying time")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 100)  # Some number

        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Please, connect your D flip-flop")

    def delay_change_of_state(self, your_input: str, delaying_time_in_sec: int) -> str:
        beginning_state: str = "State: input state"
        print(beginning_state)
        print(f"Your input: {your_input}")

        for sec in range(self._max_delaying_time_in_sec):  # 'sec' can't be more than our max del time
            print(sec)

            # If 'sec' reach func parameter - creating new state
            if sec == delaying_time_in_sec:
                print("Time has been successfully passed")
                print("Device state has changed")
                new_state = "New state"

                return new_state  # Returning new state of device
            else:
                print("Please, wait")


class RSFlipFlop(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 storing_digit: int = 1) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._storing_digit = storing_digit

    def __str__(self) -> str:
        return (f"RS flip-flop '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Temporarily storing '{self._storing_digit}' digit")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 95)  # Some number

        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Please, connect your RS flip-flop")

    def store_digit(self, time_in_sec: int) -> int:
        print(f"Holding '{self._storing_digit}' digit")

        for sec in range(time_in_sec + 1):  # Reaching 'time_in_sec' value adding 1
            print(f"{sec} sec")

            if sec is time_in_sec:
                print(f"Storing time of '{self._storing_digit}' digit has passed")

                return self._storing_digit


class ShiftRegister(DigitalElement):

    def __init__(self, name: str, purchase_cost_in_usd: int, working_time_in_years: int,
                 num_of_parallel_lines: int, is_storing_digit_possible: bool = True) -> None:
        super().__init__(name, purchase_cost_in_usd, working_time_in_years)
        self._num_of_parallel_lines = num_of_parallel_lines
        self._is_storing_digit_possible = is_storing_digit_possible

    def __str__(self) -> str:
        return (f"Shift register '{self._name}' works {self._working_time_in_years} years and costs "
                f"{self._purchase_cost_in_usd}$. Number of parallel lines: {self._num_of_parallel_lines}."
                f" Temporarily storing a digit? {self._is_storing_digit_possible}")

    def meter(self, is_connected: bool) -> int | str:
        output = random.randint(1, 80)  # Some diff number

        if is_connected:
            return output
        else:
            return "Connect your device before the measurement"

    def print_metered_info(self, device_has_been_used: bool) -> None:
        if device_has_been_used:
            # Using another func to print info
            print(f"Out: {self.meter(True)}")
        else:
            print("Please, connect your shift register")

    def store_digit(self, time_in_sec: int, digit_to_be_stored: int) -> int:

        # Doing it only if storing is possible
        if self._is_storing_digit_possible:
            print(f"Storing '{digit_to_be_stored}' digit for {time_in_sec} sec")

            for sec in range(time_in_sec + 1):  # Reaching 'time_in_sec' variable
                print(sec)

                if sec == time_in_sec:
                    print("Holding time has already passed")

                    return digit_to_be_stored  # Returning stored digit
        else:
            print("Your shift register not storing a digit")

    def make_single_input_from_parallel_lines(self) -> str:
        print(f"Number of parallel lines - {self._num_of_parallel_lines}")  # Remainder

        print("Input example: 011(1) 101(2)...")  # Some example
        user_input = input("Write all parallel lines here, like in example above: ")

        # Forming our result
        user_input_list = user_input.split()  # Creating list[int]
        result = "".join(user_input_list)  # Joining all elements

        # Printing and returning result
        print(f"Single input: {result}")

        return result
