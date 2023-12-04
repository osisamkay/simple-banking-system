### README.md

# Simple Banking System with Object-Oriented Programming

This repository contains a simple console-based banking system implemented using Object-Oriented Programming (OOP) principles in Python. The system allows users to open new accounts, access existing accounts, make deposits, make withdrawals, view account balances, and view transaction history.

## Getting Started

To run the program, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/osisamkay/simple-banking-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-banking-system
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

## Features

- Open a new account
- Access an existing account
- Make deposits
- Make withdrawals
- View account balances
- View transaction history

## Object-Oriented Programming (OOP) Principles

This project follows the four pillars of Object-Oriented Programming:

1. **Encapsulation:** The implementation of classes (`Account` and `SavingsAccount`) encapsulates the related attributes and methods into objects. The internal details of how an account works are hidden from the external world.

2. **Abstraction:** Abstract classes (`Account`) define a common interface for all types of bank accounts. The details of the account implementation are abstracted away, providing a clear separation between what an account does and how it does it.

3. **Inheritance:** The `SavingsAccount` class inherits from the abstract `Account` class. Inheritance promotes code reuse, allowing the `SavingsAccount` to inherit common methods and attributes from the base class.

4. **Polymorphism:** Polymorphism is demonstrated through method overriding in the `SavingsAccount` class. Methods such as `deposit`, `withdraw`, `view_account_balance`, and `view_transaction_history` provide different implementations specific to the savings account.

## Contributing

If you have suggestions or find issues, feel free to open an [issue](https://github.com/your-username/simple-banking-system/issues) or create a [pull request](https://github.com/your-username/simple-banking-system/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

