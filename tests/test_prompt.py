from src.cli.prompt import select_base


def test_input_value():
    # Test if the input is not an empty string or null
    selected_base = select_base()
    assert selected_base["input"] != "" or None
