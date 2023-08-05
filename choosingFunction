bases=[2,8,10,16]

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
        print("What Base Would You Like To Convert To?",available_bases,end=": ")
        choice_2=input("")
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
print(choice_2)
