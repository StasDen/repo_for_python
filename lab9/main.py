# Importing necessary stuff
from lab9.digital_elements import BinaryCounter, ReverseCounter, Multiplexer, DelayFlipFlop, RSFlipFlop, ShiftRegister


def main():
    # Binary counter
    bc = BinaryCounter("Binary counter", 200, 3, 20)
    print(bc)

    bc.meter(True)
    bc.print_metered_info(True)

    print("---------------------")

    # Reverse counter
    rc = ReverseCounter("Reverse counter", 150, 4)
    print(rc)

    rc.reverse_sequence_of_bytes()

    print("---------------------")

    # Multiplexer
    m = Multiplexer("Multiplexer", 115, 7, 3)
    print(m)

    m.forward_lines_to_single_output()

    print("---------------------")

    # D flip-flop
    dff = DelayFlipFlop("Delay flip-flop", 400, 8, 45)
    print(dff)

    dff.delay_change_of_state("0110", 21)

    print("---------------------")

    # RS flip-flop
    r_s_flip_flop = RSFlipFlop("RS flip-flop", 250, 5, 0)
    print(r_s_flip_flop)

    r_s_flip_flop.store_digit(15)

    print("---------------------")

    # Shift register
    sr = ShiftRegister("Shift register", 500, 7, 5, True)
    print(sr)

    sr.store_digit(7, 1)
    sr.make_single_input_from_parallel_lines()


if __name__ == '__main__':
    main()
