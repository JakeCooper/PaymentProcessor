#Payment Processor

The enclosed files implement a payment processor in Python. The application runs using the Python 2.X version, and has not been tested using Python 3.X. The payment processor supports the following operations:

**Add:** Adds a user with a credit card and limit. [Processor.addCard(user, cardNum, limit)]

**Charge:** Charges the user a specified amount, resulting in debt being accrued. [Processor.chargeCard(user, charge)]

**Credit:** Credits the user a specified amount, resulting in debt being removed. [Processor.creditCard(user, credit)]

Sample inputs can be found in testFile.txt

### Design Decisions

The architecture is straightforward: A hashmap (dictionary in Python) which contains keys for each user which maps to their respective UserData item. The UserData object contains their limit, card number, and current balance. The hashmap is used as it provides O(1) time for the Add, Charge, and Credit functionality. However, to print out summary at the end we require O(nlogn) time. The hashmap option was chosen by weighing each of the functions arbitrarily based on the number of runs projected. Since it is likely that more than one add, charge, and credit will be performed for each print, the hashmap is the current best implementation. 

The user's name is used as the key for the hashmap. Ideally the key would be a more unique entity, such as the credit card number. However, the sample input data given for Charge and Credit does not contain the credit card number. This solution is limited as there can only exist one user with a specific name at each time. This could be alleviated with the user of separate chaining when hashing the users, with the caveat that it may affect the worst case runtime of the hashmap.

### Programming Language Decision

Python was chosen for this project for three reasons. Primarily, it is simple, quick, and easy to produce polished code. Secondly, the unittest framework is part of the Python standard library. Finally, no additional dependencies must be installed.

### How to run

**Payment Processor**

The payment processors accepts file input using STDIN or a specified file. Either of the following commands will work:

 
```
python processor.py textfile.txt
```

```
python processor.py < textfile.txt
```

**Unit Tests**

Unit tests are run with the following command:

```
python unit.py
```
