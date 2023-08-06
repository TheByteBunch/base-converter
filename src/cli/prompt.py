import inquirer
from src.bases.base_names import Base


def select_base() -> dict[str, str]:
    """prompts the user to select a base

    Returns:
        dict[str, str]: user selected base
    """
    base_list = [
        inquirer.List(
            "input",
            message="Select base",
            choices=[base.value for base in Base],
        ),
    ]

    answer = inquirer.prompt(base_list)

    return answer
