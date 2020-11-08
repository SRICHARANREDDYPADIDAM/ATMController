class ATMController:
    def __init__(self):
        self.verification = {
            "122134534123": 2330,
            "234554679876": 1023,
            "998767875432": 2020,
        }
        self.currentAccount = None

    # check if the entered pin is correct or not
    def verify_pin(self, Account, pin):
        if self.verification[Account.id] == pin:
            self.currentAccount = Account
            return True
        else:
            self.currentAccount = None
            return False

    # check the balance of the selected account if the entered pin is correct
    def check_balance(self):
        balance = 0
        if self.currentAccount.account_mode == "checking":
            balance = self.currentAccount.checking_bal
        else:
            balance = self.currentAccount.savings_bal
        return balance

    # deposit amount in to the selected account
    def deposit_amount(self, amount):
        balance = 0
        if self.currentAccount.account_mode == "checking":
            self.currentAccount.checking_bal += amount
            balance = self.currentAccount.checking_bal
        else:
            self.currentAccount.savings_bal += amount
            balance = self.currentAccount.savings_bal
        return balance

    # withdraw amount from the account if the balance is more than the entered amount
    def withdraw_amount(self, amount):
        balance = 0
        if self.currentAccount.account_mode == "checking":
            balance = self.currentAccount.checking_bal - amount
            if balance < 0:
                return -1
            self.currentAccount.checking_bal = balance
        else:
            balance = self.currentAccount.savings_bal - amount
            if balance < 0:
                return -1
            self.currentAccount.savings_bal = balance
        return balance


class Account:
    def __init__(
        self, name, id, checking_bal=0, savings_bal=0, account_mode="checking"
    ):
        self.name = name
        self.id = id
        self.checking_bal = checking_bal
        self.savings_bal = savings_bal
        self.account_mode = account_mode

    def set_mode(self, mode):
        allowed_modes = ["checking", "savings"]
        if mode.lower() not in allowed_modes:
            print("Incorrect account mode")
            return False
        self.account_mode = mode


# test cases to check some of the important operations of an ATM
def test_1_correct_pin_check_balance():
    print("=" * 50)
    print("Test 1:\nThis test will input the correct pin and check the balance")
    print("=" * 50)
    charan = Account(name="charan", id="234554679876", savings_bal=1000)

    ok = controller.verify_pin(charan, 1023)
    if not ok:
        exit()
    charan.set_mode("savings")
    print("Savings account balance is: " + str(controller.check_balance()))
    print("")


def test_2_incorrect_pin():
    print("=" * 50)
    print("Test 2:\nThis test will input an incorrect pin")
    print("=" * 50)
    john = Account(name="John", id="122134534123")
    ok = controller.verify_pin(john, 1234)
    if not ok:
        print("You have entered incorrect pin")
    else:
        print("This will never be printed")
    print("")


def test_3_deposit_balance():
    print("=" * 50)
    print("Test 3:\nThis test will deposit some balance")
    print("=" * 50)
    jack = Account(name="jack", id="234554679876", checking_bal=1000)

    ok = controller.verify_pin(jack, 1023)
    if not ok:
        exit()
    jack.set_mode("checking")
    print("Current Checkings account balance is: " + str(controller.check_balance()))
    controller.deposit_amount(500)
    print("New Checkings account balance is: " + str(controller.check_balance()))
    print("")


def test_4_withdraw_balance():
    print("=" * 50)
    print("Test 4:\nThis test will withdraw some balance")
    print("=" * 50)
    paul = Account(name="paul", id="122134534123", checking_bal=1000)
    ok = controller.verify_pin(paul, 2330)
    if not ok:
        print("You havbe entered incorrect pin")
    paul.set_mode("checking")
    print("Current Checkings account balance is: " + str(controller.check_balance()))
    controller.withdraw_amount(500)
    print("New Checkings account balance is: " + str(controller.check_balance()))
    print("")


def test_5_withdraw_insufficient():
    print("=" * 50)
    print(
        "Test 5:\nThis test will try to withdraw balance\nbut will fail due to insufficient funds"
    )
    print("=" * 50)
    paul = Account(name="paul", id="122134534123", savings_bal=500)
    ok = controller.verify_pin(paul, 2330)
    if not ok:
        print("You havbe entered incorrect pin")
    paul.set_mode("Savings")
    print("Current savings account balance is: " + str(controller.check_balance()))
    new_balance = controller.withdraw_amount(1500)
    if new_balance < 0:
        print("Insufficient funds, your balance is: " + str(controller.check_balance()))
    else:
        print("This will never be printed")
    print("")


if __name__ == "__main__":
    controller = ATMController()
    test_1_correct_pin_check_balance()
    test_2_incorrect_pin()
    test_3_deposit_balance()
    test_4_withdraw_balance()
    test_5_withdraw_insufficient()
