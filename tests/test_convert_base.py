from src.core.convert import convert_base

# Binary to other bases


def test_bin_to_bin():
    result = convert_base("1001", 2, 2)
    assert result == "1001"


def test_bin_to_oct():
    result = convert_base("1101", 2, 8)
    assert result == "15"


def test_bin_to_dec():
    result = convert_base("1100", 2, 10)
    assert result == "12"


def test_bin_to_hex():
    result = convert_base("1111", 2, 16)
    assert result == "F"

# Octal to other bases


def test_oct_to_oct():
    result = convert_base("73", 8, 8)
    assert result == "73"


def test_oct_to_bin():
    result = convert_base("73", 8, 2)
    assert result == "111011"


def test_oct_to_dec():
    result = convert_base("73", 8, 10)
    assert result == "59"


def test_oct_to_hex():
    result = convert_base("73", 8, 16)
    assert result == "3B"

# Decimal to other bases


def test_dec_to_dec():
    result = convert_base("94", 10, 10)
    assert result == "94"


def test_dec_to_bin():
    result = convert_base("94", 10, 2)
    assert result == "1011110"


def test_dec_to_oct():
    result = convert_base("94", 10, 8)
    assert result == "136"


def test_dec_to_hex():
    result = convert_base("94", 10, 16)
    assert result == "5E"

# Hexadecimal to other bases


def test_hex_to_hex():
    result = convert_base("DEA5", 16, 16)
    assert result == "DEA5"


def test_hex_to_bin():
    result = convert_base("DEA5", 16, 2)
    assert result == "1101111010100101"


def test_hex_to_oct():
    result = convert_base("DEA5", 16, 8)
    assert result == "157245"


def test_hex_to_dec():
    result = convert_base("DEA5", 16, 10)
    assert result == "56997"
