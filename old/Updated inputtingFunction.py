bases=[2,8,10,16]
binary_digits=[0,1]
octal_digits=[0,1,2,3,4,5,6,7]
decimal_digits=[0,1,2,3,4,5,6,7,8,9]
hex_digits=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
out=False
def choosing(bases):
    while True:
        choice=input("What Base Would You Like To Convert From [2, 8, 10 ,16]: ")
        if not choice.isdigit():
            print("Input Must Be A Number, Please Try Again.")
            continue
        choice=int(choice)
        if choice not in bases:
            print("Not A Choice, Please Try Again.")
            continue
        break
    return choice
choice=choosing(bases)
available_bases = list(filter(lambda b: b != choice, bases))
def choosing_2(choice):
    while True:
        choice_2=input(f"What Base Would You Like To Convert To? {available_bases}: ")
        if not choice_2.isdigit():
            print("Input Must Be A Number, Please Try Again.")
            continue
        choice_2=int(choice_2)
        choice_2=int(choice_2)
        if choice_2 not in bases:
            print("Choice Does Not Exist, Please Try Again.")
            continue
        if choice_2==choice:
            print("Cannot Convert To Same Base, Please Try Again.")
            continue
        break
    return choice_2
choice_2=choosing_2(choice)
def inputting_number(choice,out):
    while True:
        number=input(f"Please Input A Base {choice} Number: ")
        if not number.isdigit() and choice!=16:
            print("Input Must Be A Number.")
            continue
        if choice in [2,8,10]:
            number=int(number)
        if choice==2:
            for digit in str(number):
                if digit not in str(binary_digits):
                    print("Please Input A Valid Base 2 Number.")
                    out=True
                    break
        if choice==8:
            for digit in str(number):
                if digit not in str(octal_digits):
                    print("Please Input A Valid Base 8 Number.")
                    out=True
                    break
        if choice==10:
            for digit in str(number):
                if digit not in str(decimal_digits):
                    print("Please Input A Valid Base 10 Number.")
                    out=True
                    break
        if choice==16:
            for digit in str(number):
                if digit not in str(hex_digits):
                    print("Please Input A Valid Base 16 Number.")
                    out=True
                    break
        if out==True:
            continue
        break
    return number
number=inputting_number(choice,out)
print(number)
