from abc import abstractmethod, ABCMeta
from datetime import datetime
from random import randint


class Account(metaclass=ABCMeta):
    """
    Abstract base class representing a generic bank account.
    """

    @abstractmethod
    def open_new_account(self, name, initial_deposit):
        """
        Opens a new bank account.

        Parameters:
        - name (str): The name of the account holder.
        - initial_deposit (float): The initial deposit amount.

        Returns:
        - int: The generated account number.
        """
        pass

    @abstractmethod
    def generate_account_number(self):
        """
        Generates a unique account number.

        Returns:
        - int: The generated account number.
        """
        pass

    @abstractmethod
    def retrieve_account(self, account_number):
        """
        Retrieves information about a specific account.

        Parameters:
        - account_number (int): The account number to retrieve.

        Returns:
        - dict or None: A dictionary containing account information, or None if the account is not found.
        """
        pass


class SavingsAccount(Account):
    """
    Concrete class representing a savings account, inheriting from the Account base class.
    """

    def __init__(self):
        """
        Initializes a new SavingsAccount instance with empty account and transaction history.
        """
        self.savings_accounts = {}
        self.transaction_history = {}
        self.current_account_number = None
        self.account_counter = randint(1000000000, 9999999999)

    def open_new_account(self, name, initial_deposit):
        """
        Opens a new savings account.

        Parameters:
        - name (str): The name of the account holder.
        - initial_deposit (float): The initial deposit amount.

        Returns:
        - int: The generated account number.
        """
        account_number = self.generate_account_number()
        self.savings_accounts[account_number] = {"name": name, "balance": initial_deposit}
        self.transaction_history[account_number] = [
            {"type": "Opening", "amount": initial_deposit, "timestamp": datetime.now()}
        ]
        return account_number

    def generate_account_number(self):
        """
        Generates a unique account number.

        Returns:
        - int: The generated account number.
        """
        return self.account_counter

    def retrieve_account(self, account_number):
        """
        Retrieves information about a specific savings account.

        Parameters:
        - account_number (int): The account number to retrieve.

        Returns:
        - dict or None: A dictionary containing account information, or None if the account is not found.
        """
        return self.savings_accounts.get(account_number, None)

    def deposit(self, amount_deposit):
        """
        Makes a deposit into the current savings account.

        Parameters:
        - amount_deposit (float): The amount to deposit.

        Returns:
        - bool: True if the deposit is successful, False otherwise.
        """
        if self.current_account_number in self.savings_accounts:
            self.savings_accounts[self.current_account_number]["balance"] += amount_deposit
            self.transaction_history[self.current_account_number].append(
                {"type": "Deposit", "amount": amount_deposit, "timestamp": datetime.now()}
            )
            return True
        return False

    def withdraw(self, amount_withdraw):
        """
        Makes a withdrawal from the current savings account.

        Parameters:
        - amount_withdraw (float): The amount to withdraw.

        Returns:
        - bool: True if the withdrawal is successful, False otherwise.
        """
        if self.current_account_number in self.savings_accounts:
            if self.savings_accounts[self.current_account_number]["balance"] >= amount_withdraw:
                self.savings_accounts[self.current_account_number]["balance"] -= amount_withdraw
                self.transaction_history[self.current_account_number].append(
                    {"type": "Withdrawal", "amount": amount_withdraw, "timestamp": datetime.now()}
                )
                return True
        return False

    def view_account_balance(self):
        """
        Views the current balance of the savings account.

        Returns:
        - float or None: The current balance, or None if there's an error fetching the balance.
        """
        return self.savings_accounts.get(self.current_account_number, {}).get("balance", None)

    def view_transaction_history(self):
        """
        Views the transaction history of the savings account.

        Returns:
        - list: A list of dictionaries representing transaction history.
        """
        return self.transaction_history.get(self.current_account_number, [])


# Simple console interface
def main():
    """
    Main function to run the simple console-based banking system.
    """
    savings_account = SavingsAccount()

    while True:
        print("\n1. Open a new account")
        print("2. Access an existing account")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter the initial deposit amount: "))
            account_number = savings_account.open_new_account(name, initial_deposit)
            print(f"\nAccount created successfully! Your account number is: {account_number}")

        elif choice == "2":
            if savings_account.current_account_number is None:
                account_number = int(input("Enter your account number: "))
                account_info = savings_account.retrieve_account(account_number)

                if account_info:
                    savings_account.current_account_number = account_number
                    print("\nAccount accessed successfully!")

                else:
                    print("Account not found. Please check your account number.")

            else:
                print(f"You are already logged in with account number {savings_account.current_account_number}")

        elif choice == "3":
            print("Quitting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        # Sub-menu for logged-in users
        while savings_account.current_account_number is not None:
            print("\nLogged-in Menu:")
            print("1. Make a deposit")
            print("2. Make a withdrawal")
            print("3. View account balance")
            print("4. View transaction history")
            print("5. Log out")
            print("6. Quit")

            sub_choice = input("Enter your choice (1/2/3/4/5/6): ")

            if sub_choice == "1":
                amount_deposit = float(input("Enter the deposit amount: "))
                if savings_account.deposit(amount_deposit):
                    print("Deposit successful!")
                else:
                    print("Error making deposit. Please try again.")

            elif sub_choice == "2":
                amount_withdraw = float(input("Enter the withdrawal amount: "))
                if savings_account.withdraw(amount_withdraw):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds or error making withdrawal. Please try again.")

            elif sub_choice == "3":
                balance = savings_account.view_account_balance()
                if balance is not None:
                    print(f"Account Balance: ${balance:.2f}")
                else:
                    print("Error fetching account balance. Please try again.")

            elif sub_choice == "4":
                history = savings_account.view_transaction_history()
                if history:
                    print("\nTransaction History:")
                    for transaction in history:
                        print(f"{transaction['timestamp']}: {transaction['type']} - ${transaction['amount']:.2f}")
                else:
                    print("No transaction history available.")

            elif sub_choice == "5":
                savings_account.current_account_number = None
                print("Logged out successfully!")
                break

            elif sub_choice == "6":
                print("Quitting the program.")
                exit()

            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
