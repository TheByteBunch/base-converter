from sys import path
from src.cli.prompt import select_base
from src.utils.validator import Validator
from src.core.convert import convert_base


def main():
    origin_base = select_base()
    entered_number = input("Enter number:")

    Validator.validate_input(entered_number, origin_base)

    destination_base = select_base()

    converted_number = convert_base(
        entered_number, origin_base, destination_base)
    print(converted_number)


if __name__ == "__main__":
    path.append('../')
    main()
