
account_database = {
    'food': 4000,
    'clothing': 2500,
    'entertainment': 2000,
    'miscellaneous': 3000
}


def user_balance(user_category):
    if user_category == 'food':
        account_balance = account_database['food']
        return account_balance

    elif user_category == 'clothing':
        account_balance = account_database['clothing']
        return account_balance

    elif user_category == 'entertainment':
        account_balance = account_database['entertainment']
        return account_balance

    elif user_category == 'miscellaneous':
        account_balance = account_database['miscellaneous']
        return account_balance


def food_database(user_amount):
    food_balance = user_amount + account_database['food']
    account_database.update({'food': food_balance})
    return food_balance


def clothing_database(user_amount):
    clothing_balance = user_amount + account_database['clothing']
    account_database.update({'clothing': clothing_balance})
    return clothing_balance


def entertainment_database(user_amount):
    entertainment_balance = user_amount + account_database['entertainment']
    account_database.update({'entertainment': entertainment_balance})
    return entertainment_balance


def miscellaneous_database(user_amount):
    miscellaneous_balance = user_amount + account_database['miscellaneous']
    account_database.update({'miscellaneous': miscellaneous_balance})
    return miscellaneous_balance

