# ATMController
ATM Controller implemented in python

## Running Instructions
Clone the project
```shell
git clone https://github.com/SRICHARANREDDYPADIDAM/ATMController.git
```
Execute using python
```shell
cd ATMController
python Controller.py
```

## Sample Output
```shell
sricharanreddypadidam@Charans-MBP ATMController % python Controller.py
==================================================
Test 1:
This test will input the correct pin and check the balance
==================================================
Savings account balance is: 1000

==================================================
Test 2:
This test will input an incorrect pin
==================================================
You have entered incorrect pin

==================================================
Test 3:
This test will deposit some balance
==================================================
Current Checkings account balance is: 1000
New Checkings account balance is: 1500

==================================================
Test 4:
This test will withdraw some balance
==================================================
Current Checkings account balance is: 1000
New Checkings account balance is: 500

==================================================
Test 5:
This test will try to withdraw balance
but will fail due to insufficient funds
==================================================
Current savings account balance is: 500
Insufficient funds, your balance is: 500
```
