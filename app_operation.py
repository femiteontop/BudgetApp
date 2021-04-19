import budget_app


def init():
    print('==' * 15 + ' BUDGET APP ' + '==' * 15 + '\n')
    print("1. Food \n2. Clothing\n3. Entertainment \n4. Miscellaneous \n5. Logout \n")
    user_budget = int(input("Select a budget from options above: \n"))

    if user_budget == 1:
        food()

    elif user_budget == 2:
        clothing()

    elif user_budget == 3:
        entertainment()

    elif user_budget == 4:
        miscellaneous()

    elif user_budget == 5:
        exit()

    else:
        print('Invalid option selected, try again')
        init()


def food():
    print('==' * 15 + ' FOOD BUDGET ' + '==' * 15 + '\n')
    print('1. Deposit \n2. Withdraw \n3. Check Balance \n4. Transfer \n')
    food_task = int(input('Choose one option from above: \n'))

    if food_task == 1:
        user_amount = int(input("Enter amount to deposit: \n"))
        result = budget_app.Budget('food').deposit(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            food()

    elif food_task == 2:
        user_amount = int(input("Enter amount to withdraw: \n"))
        result = budget_app.Budget('food').withdraw(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            food()

    elif food_task == 3:
        result = budget_app.Budget('food').check_balance()
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            food()

    elif food_task == 4:
        user_amount = int(input("Enter amount to transfer: \n"))
        recipient_category = input('Kindly enter category to transfer to; \n'
                                   'clothing or entertainment or miscellaneous.\n')
        result = budget_app.Budget('food').transfer(user_amount, recipient_category)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            food()

    else:
        print('Invalid option selected: ')
        food()


def clothing():
    print('==' * 15 + ' CLOTHING BUDGET ' + '==' * 15 + '\n')
    print('1. Deposit \n2. Withdraw \n3. Check Balance \n4. Transfer \n')
    clothing_task = int(input('Choose one option from above: \n'))

    if clothing_task == 1:
        user_amount = int(input("Enter amount to deposit: \n"))
        result = budget_app.Budget('clothing').deposit(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            clothing()

    elif clothing_task == 2:
        user_amount = int(input("Enter amount to withdraw: \n"))
        result = budget_app.Budget('clothing').withdraw(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            clothing()

    elif clothing_task == 3:
        result = budget_app.Budget('clothing').check_balance()
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            clothing()

    elif clothing_task == 4:
        user_amount = int(input("Enter amount to transfer: \n"))
        recipient_category = input('Kindly enter category to transfer to; \n'
                                   'food or entertainment or miscellaneous.\n')
        result = budget_app.Budget('clothing').transfer(user_amount, recipient_category)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            clothing()

    else:
        print('Invalid option selected: ')
        clothing()


def entertainment():
    print('==' * 15 + ' ENTERTAINMENT BUDGET ' + '==' * 15 + '\n')
    print('1. Deposit \n2. Withdraw \n3. Check Balance \n4. Transfer \n')
    entertainment_task = int(input('Choose one option from above: \n'))

    if entertainment_task == 1:
        user_amount = int(input("Enter amount to deposit: \n"))
        result = budget_app.Budget('entertainment').deposit(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            entertainment()

    elif entertainment_task == 2:
        user_amount = int(input("Enter amount to withdraw: \n"))
        result = budget_app.Budget('entertainment').withdraw(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            entertainment()

    elif entertainment_task == 3:
        result = budget_app.Budget('entertainment').check_balance()
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            entertainment()

    elif entertainment_task == 4:
        user_amount = int(input("Enter amount to transfer: \n"))
        recipient_category = input('Kindly enter category to transfer to; \n'
                                   'food or clothing or miscellaneous.\n')
        result = budget_app.Budget('entertainment').transfer(user_amount, recipient_category)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            entertainment()

    else:
        print('Invalid option selected: ')
        entertainment()


def miscellaneous():
    print('==' * 15 + ' MISCELLANEOUS BUDGET ' + '==' * 15 + '\n')
    print('1. Deposit \n2. Withdraw \n3. Check Balance \n4. Transfer \n')
    miscellaneous_task = int(input('Choose one option from above: \n'))

    if miscellaneous_task == 1:
        user_amount = int(input("Enter amount to deposit: \n"))
        result = budget_app.Budget('miscellaneous').deposit(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            miscellaneous()

    elif miscellaneous_task == 2:
        user_amount = int(input("Enter amount to withdraw: \n"))
        result = budget_app.Budget('miscellaneous').withdraw(user_amount)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            miscellaneous()

    elif miscellaneous_task == 3:
        result = budget_app.Budget('miscellaneous').check_balance()
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            miscellaneous()

    elif miscellaneous_task == 4:
        user_amount = int(input("Enter amount to transfer: \n"))
        recipient_category = input('Kindly enter category to transfer to; \n'
                                   'food or clothing or entertainment.\n')
        result = budget_app.Budget('miscellaneous').transfer(user_amount, recipient_category)
        print(result)

        another_task = int(input('\nDo you want to perform another task? \n1. Yes \n2. No \n'))
        if another_task == 1:
            init()

        elif another_task == 2:
            exit()

        else:
            print('Invalid option selected, try again.')
            miscellaneous()

    else:
        print('Invalid option selected: ')
        miscellaneous()


init()

