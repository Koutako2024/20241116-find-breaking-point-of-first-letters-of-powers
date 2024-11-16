import math
from collections.abc import Generator


def main() -> None:
    max_exponent: int = int(input("Press max>"))
    first_letters_gen: Generator[int] = powers_first_letters_generator()
    guessed_cycle: list[int] = [int(c) for c in "2481361251"]
    for i in range(max_exponent):
        if next(first_letters_gen) != guessed_cycle[i % len(guessed_cycle)]:
            print(f"This cycle got broken at 2^{i+1}.")
            return
    print(f"I couldn't find its breaking by {max_exponent}.")


def powers_first_letters_generator(
    counting_base: int = 10, power_base: int = 2
) -> Generator[int]:
    exponent: int = 1
    while True:
        num_len: int = math.floor(math.log(power_base**exponent, counting_base))

        for top_num in range(1, counting_base):
            # top_num * counting_base ** num_len <= power_base ** exponent < (top_num + 1) * counting_base ** num_len
            if math.log(top_num, counting_base) + num_len <= exponent * math.log(
                power_base, counting_base
            ) and math.log(top_num + 1, counting_base) + num_len > exponent * math.log(
                power_base, counting_base
            ):
                break

        yield top_num
        # print(f"{power_base} ** {exponent} = {top_num}...")

        exponent += 1


if __name__ == "__main__":
    main()
