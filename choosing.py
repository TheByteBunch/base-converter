def choose_from_base(bases):
    while True:
        choice = input(f"What Base Would You Like To Convert From {bases}: ")
        if not choice.isdigit():
            print("Input Must Be A Number, Please Try Again.")
            continue
        choice = int(choice)
        if choice not in bases:
            print("Not A Choice, Please Try Again.")
            continue
        break
    return choice


def choose_to_base(from_base, bases):

    available_bases = []
    for base in bases:
        if base != from_base:
            available_bases.append(base)

    while True:
        choice_2 = input(f"What Base Would You Like To Convert To? {available_bases}: ")
        if not choice_2.isdigit():
            print("Input Must Be A Number, Please Try Again.")
            continue
        choice_2 = int(choice_2)
        if choice_2 not in available_bases:
            print("Choice Does Not Exist, Please Try Again.")
            continue
        # if choice_2 == choice:  # we've already checked this by not putting from_base in available_bases
        #     print("Cannot Convert To Same Base, Please Try Again.")
        #     continue
        break
    return choice_2


def choose_input_number(from_base):
    number = input(f"Please Input A Base {from_base} Number: ")
    return number

    # Let's move this validation logic out of the input functions
    # if not number.isdigit() and choice!=16:
    #     print("Input Must Be A Number.")
    #     continue
    # if choice in [2,8,10]:
    #     number = int(number)
    # if choice == 2:
    #     for digit in str(number):
    #         if digit not in str(binary_digits):
    #             print("Please Input A Valid Base 2 Number.")
    #             out=True
    #             break
    # if choice==8:
    #     for digit in str(number):
    #         if digit not in str(octal_digits):
    #             print("Please Input A Valid Base 8 Number.")
    #             out=True
    #             break
    # if choice==10:
    #     for digit in str(number):
    #         if digit not in str(decimal_digits):
    #             print("Please Input A Valid Base 10 Number.")
    #             out=True
    #             break
    # if choice==16:
    #     for digit in str(number):
    #         if digit not in str(hex_digits):
    #             print("Please Input A Valid Base 16 Number.")
    #             out=True
    #             break
    # if out==True:
    #     continue

