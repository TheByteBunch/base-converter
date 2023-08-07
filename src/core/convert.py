def convert_base(number: str, origin_base: int, destination_base: int) -> str:
    if origin_base == destination_base:
        return number
    converted_number = ""
    number = str(int(number, base=origin_base))

    if destination_base == 2:
        converted_number = bin(int(number))[2:]
    elif destination_base == 8:
        converted_number = oct(int(number))[2:]
    elif destination_base == 10:
        converted_number = number
    elif destination_base == 16:
        converted_number = hex(int(number)).upper()[2:]
    return converted_number
