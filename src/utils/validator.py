import re


class Validator:
    @staticmethod
    def is_valid_base(number: str, base: int) -> bool:
        if base < 16:
            pattern = rf'^[0-{base - 1}]$'
        else:
            pattern = r'^[0-9A-Fa-f]+$'

        return re.match(pattern, number) is not None

    @staticmethod
    def validate_input(entered_number: str, selected_base: int):
        for digit in entered_number:
            if not Validator.is_valid_base(digit, selected_base):
                raise ValueError()
