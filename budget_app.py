"""
Budget App

Create a Budget class that can instantiate objects based on different budget categories like food, clothing,
and entertainment. These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories

Push your code to GitHub, and submit the repo link.
"""
import database


class Budget:
    def __init__(self, category):
        self.balance = database.user_balance(category)
        self.category = category

    def deposit(self, amount):
        self.balance += amount

        return f"Your new balance for {self.category} budget is ₦{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Unable to withdraw for {self.category} budget due to insufficient balance, " \
                   f"₦{amount} you entered is more than your balance of ₦{self.balance}."

        else:
            self.balance -= amount
            return f"Successfully withdraw ₦{amount}, your new balance for {self.category} budget is ₦{self.balance}."

    def check_balance(self):

        return f"Your budget balance is ₦{self.balance}"

    def transfer(self, amount, transfer_receiver):
        if transfer_receiver == 'food':
            receiver_balance = database.food_database(amount)

            if transfer_receiver == self.category:
                response = f"You can not transfer from {transfer_receiver} budget to {self.category} budget \n"
                response += f"{'###' * 20} \nThey are the same!!! \n"
                response += f"{'###' * 20} \nChange budget recipient."
                return response

            elif amount > self.balance:
                return f"Unable to transfer from {self.category} budget to {transfer_receiver} budget " \
                       f"due to insufficient balance, \n{'###' * 20} \n" \
                       f"₦{amount} you entered is more than your balance of ₦{self.balance}"

            elif amount <= self.balance:
                self.balance -= amount

                return f"₦{amount} transferred successfully into {transfer_receiver} budget from {self.category} budget." \
                       f" \n{'###' * 20} \n" \
                       f"Your new balance for {self.category} budget is ₦{self.balance}. \n{'###' * 20} \n" \
                       f"Your new balance for {transfer_receiver} budget is ₦{receiver_balance}"

            else:
                exit()

        elif transfer_receiver == 'clothing':
            receiver_balance = database.clothing_database(amount)

            if transfer_receiver == self.category:
                response = f"You can not transfer from {transfer_receiver} budget to {self.category} budget \n"
                response += f"{'###' * 20} \nThey are the same!!! \n"
                response += f"{'###' * 20} \nChange budget recipient."
                return response

            elif amount > self.balance:
                return f"Unable to transfer from {self.category} budget to {transfer_receiver} budget " \
                       f"due to insufficient balance, \n{'###' * 20} \n" \
                       f"₦{amount} you entered is more than your balance of ₦{self.balance}"

            elif amount <= self.balance:
                self.balance -= amount

                return f"₦{amount} transferred successfully into {transfer_receiver} budget from {self.category} budget." \
                       f" \n{'###' * 20} \n" \
                       f"Your new balance for {self.category} budget is ₦{self.balance}. \n{'###' * 20} \n" \
                       f"Your new balance for {transfer_receiver} budget is ₦{receiver_balance}"

            else:
                exit()

        elif transfer_receiver == 'entertainment':
            receiver_balance = database.entertainment_database(amount)

            if transfer_receiver == self.category:
                response = f"You can not transfer from {transfer_receiver} budget to {self.category} budget \n"
                response += f"{'###' * 20} \nThey are the same!!! \n"
                response += f"{'###' * 20} \nChange budget recipient."
                return response

            elif amount > self.balance:
                return f"Unable to transfer from {self.category} budget to {transfer_receiver} budget " \
                       f"due to insufficient balance, \n{'###' * 20} \n" \
                       f"₦{amount} you entered is more than your balance of ₦{self.balance}"

            elif amount <= self.balance:
                self.balance -= amount

                return f"₦{amount} transferred successfully into {transfer_receiver} budget from {self.category} budget." \
                       f" \n{'###' * 20} \n" \
                       f"Your new balance for {self.category} budget is ₦{self.balance}. \n{'###' * 20} \n" \
                       f"Your new balance for {transfer_receiver} budget is ₦{receiver_balance}"

            else:
                exit()

        elif transfer_receiver == 'miscellaneous':
            receiver_balance = database.miscellaneous_database(amount)

            if transfer_receiver == self.category:
                response = f"You can not transfer from {transfer_receiver} budget to {self.category} budget \n"
                response += f"{'###' * 20} \nThey are the same!!! \n"
                response += f"{'###' * 20} \nChange budget recipient."
                return response

            elif amount > self.balance:
                return f"Unable to transfer from {self.category} budget to {transfer_receiver} budget " \
                       f"due to insufficient balance, \n{'###' * 20} \n" \
                       f"₦{amount} you entered is more than your balance of ₦{self.balance}"

            elif amount <= self.balance:
                self.balance -= amount

                return f"₦{amount} transferred successfully into {transfer_receiver} budget from {self.category} budget." \
                       f" \n{'###' * 20} \n" \
                       f"Your new balance for {self.category} budget is ₦{self.balance}. \n{'###' * 20} \n" \
                       f"Your new balance for {transfer_receiver} budget is ₦{receiver_balance}"

            else:
                exit()

        else:
            print('Wrong budget category.')
            exit()
